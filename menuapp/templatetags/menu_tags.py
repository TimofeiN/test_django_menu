from django import template
from django.db.models import Q
from django.urls import NoReverseMatch, reverse
from django.utils.safestring import mark_safe

from menuapp.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        items = MenuItem.objects.filter(parent=None, name=menu_name).order_by('id').prefetch_related('children')
        return mark_safe(render_menu(items, request))
    except MenuItem.DoesNotExist:
        return ''


def render_menu(items, request, active_item=None):
    if not items:
        return ''
    
    if not active_item:
        for item in items:
            if is_item_active(item, request):
                active_item = item

    result = '<ul>' 
    for item in items:
        if active_item: 
            if not (item.parent_id == active_item.id or item.parent_id == active_item.parent_id):
                result = ''
                return ''
        if item == active_item:
            result += '<li class="active">'
        else: 
            result += '<li>'
        
        result += '<a href="%s">%s</a>' % (get_item_url(item), item.name)
        result += render_menu(item.children.all(), request, active_item)
        result += '</li>'
        
    result += '</ul>'
    return result





def is_item_active(item, request):
    if item.url == request.path:
        return True
    

def get_item_url(item):
    try:
        return reverse(item.url)
    except NoReverseMatch:
        return item.url
