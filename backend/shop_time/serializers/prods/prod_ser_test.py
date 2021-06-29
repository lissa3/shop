from django.contrib.auth import get_user_model
# from django.core.validators import FileExtensionValidator

from rest_framework import serializers as ser
from products.models import Product


User = get_user_model()


class ProductTestSerializer(ser.ModelSerializer):    
    categ_name = ser.ReadOnlyField(source='categ.name')    
    an_likes = ser.IntegerField(read_only=True)
    avg_rate = ser.DecimalField(read_only=True, max_digits=5, decimal_places=2, default='0.00')    
    # photo = ser.ImageField(required=False, allow_null=True)    
        
    class Meta:
        model = Product
        fields = ('id', 'name','description', 'slug',
                  'categ_name', 'categ','an_likes', 'avg_rate', 'featured', 'price','compare_price','discount','sold')
        