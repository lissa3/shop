from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
   list_display = ('name','categ','price','quantity','date_created')  
   
admin.site.register(Product,ProductAdmin)


