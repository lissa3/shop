from django.contrib import admin
from .models import Category
from mptt.admin import MPTTModelAdmin



class CategoryAdmin(MPTTModelAdmin):
    mptt_indent_field = "name"
    mptt_level_indent = 20
    list_display = ('name',) 
   


admin.site.register(Category, CategoryAdmin)
 
