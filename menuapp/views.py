from django.shortcuts import render

from .models import MenuItem


def menu(request, menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    return render(request, 'menu.html', {'menu_items': menu_items})
