from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

from categories.models import Category
from myutils.helpers import upload_prod

User = get_user_model()
ALLOWED_EXTENTIONS = ('JPG', 'JPEG', 'PNG')

class Product(models.Model):
    name = models.CharField(max_length=120)
    categ = models.ForeignKey(Category,on_delete = models.CASCADE,related_name='prods')
    compare_price = models.DecimalField(max_digits=6,decimal_places=2)
    customers = models.ManyToManyField(User, 
                                related_name='cust_prods',
                                through='UserProductRelation'
                                )                        
    featured = models.BooleanField(blank=True, default=False)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2,default='0.00')
    slug = AutoSlugField(populate_from='name',unique=True)
    sold = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    photo = models.ImageField(upload_to=upload_prod,
                            blank=True,null=True,
                            validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENTIONS)]
                            )
    in_stock = models.BooleanField(default = True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class UserProductRelation(models.Model):
    RATING = (
        (1, 'OK'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Excellent')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(blank=True, default=False)
    in_bookmark = models.BooleanField(blank=True, default=False)
    rating = models.PositiveSmallIntegerField(choices=RATING, null=True, blank=True)

    def __str__(self):
        """ here user = email"""
        return f'User: {self.user} reacted at prod {self.prod.id}'