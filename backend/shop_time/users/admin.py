from django import forms
from django.contrib import admin
from django.contrib.auth.admin import AdminPasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _
from .forms import UserCreationForm,UserChangeForm


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """ attrs: is_superuser,is_active,is_staff (let op: no is_admin)"""
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id','email', 'first_name', 'last_name', 'is_active' )
    list_filter = ('is_active',)
    list_display_links = ('id','email','first_name','last_name')
    search_fields = ('email','first_name','last_name',)
    list_per_page = 25


    # add key 'classes' with value [collapse ] to toggle Important Dates
    fieldsets = (
        (_('User'), {'fields': ('first_name','is_active','last_name', 'email', 'password')}),
        (_('Permissions'), {'classes': ['collapse'], 'fields': (
            'is_superuser', 'groups', 'user_permissions',)}),
        (_('Important dates'), {'classes': ['collapse'], 'fields': ('date_joined',)}),

    )
    add_fieldsets = (
        (('Add  User'), {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name','is_active','password1', 'password2'),
        }),
    )
    ordering = ('-date_joined',)  # 'email')
    # filter_vertical = ('groups','user_permissions')
    filter_horizontal = ('groups', 'user_permissions')  # for the right widget


admin.site.register(User, UserAdmin)


