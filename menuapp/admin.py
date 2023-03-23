from django.contrib import admin

from .forms import MenuItemForm
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)
