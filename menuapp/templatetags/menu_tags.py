from django import template
from django.db.models import Q
from django.urls import NoReverseMatch, reverse
from django.utils.safestring import mark_safe

from menuapp.models import MenuItem

register = template.Library()

def draw_menu(menu_name):
    try:
        items = MenuItem.objects.filter(parent=None, name=menu_name).order_by('id')
        return mark_safe(render_menu(items))
    except MenuItem.DoesNotExist:
        return ''

def render_menu(items):
    if not items:
        return ''
    result = '<ul>'
    for item in items:
        result += '<li class="active">' if is_item_active(item) else '<li>'
        result += '<a href="%s">%s</a>' % (get_item_url(item), item.name)
        result += render_menu(item.children.all())
        result += '</li>'
    result += '</ul>'
    return result

def is_item_active(item):
    try:
        return reverse(item.url) == reverse(item.url)
    except NoReverseMatch:
        return False

def get_item_url(item):
    try:
        return reverse(item.url)
    except NoReverseMatch:
        return item.url

register.simple_tag(draw_menu)
