from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import When, Case, Count, Avg

from rest_framework import status

from categories.models import Category
from products.models import Product,UserProductRelation

from serializers.prods.prod_ser import ProductSerializer

User = get_user_model()

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="pen")
        self.user1 = User.objects.create(email="haas@mail.com")
        self.user2 = User.objects.create (email="vos@mail.com")
        self.product1 = Product.objects.create(
            name="red pen",categ=self.category,price=23.43,compare_price=24.00,
            featured = False,description="abcd"
        )
        self.product2 = Product.objects.create(
            name="black pen",categ=self.category,price=26.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.user_prod_rel1 = UserProductRelation.objects.create(
            prod=self.product1,
            user=self.user1,
            like=True,
            rating=5
        )
        self.user_prod_rel2 = UserProductRelation.objects.create(
            prod=self.product2,
            user=self.user2,
            rating=4
        )
        self.prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            )
                

    def test_single_product(self):
        """ """
        url = reverse('products:products-detail', kwargs={"slug": self.product1.slug})
        print("url in test is",url)
        response = self.client.get(url)
        prod = self.prods.filter(slug=self.product1.slug).last() 
        local_ser_data = ProductSerializer(prod).data        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data)   

    def test_product_list(self):
        """ """
        url = reverse('products:products-list')
        response = self.client.get(url)
        local_ser_data = ProductSerializer(self.prods,many=True).data        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data)    

        
      