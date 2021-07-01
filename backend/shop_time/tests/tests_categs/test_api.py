from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import  Category
from products.models import Product
from serializers.categs.serializers import CategorySerializer
from serializers.prods.prod_ser import ProductSerializer

User = get_user_model()

class CategTestCase(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="chat")
        self.category2 = Category.objects.create(name="kletskoek")
        self.category3 = Category.objects.create(name="talk", parent=self.category2)
        self.category4 = Category.objects.create(name="ha-ha", parent=self.category3)
        self.cats = Category.objects.all()
        # products
        self.product1 = Product.objects.create(
            name="red pen1",categ=self.category1,price=23.43,compare_price=24.00,
            featured = False,description="abcd"
        )
        self.product2 = Product.objects.create(
            name="black pen1",categ=self.category3,price=26.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.product3 = Product.objects.create(
            name="red pen2",categ=self.category3,price=23.43,compare_price=24.00,
            featured = False,description="abcd"
        )
        self.product4 = Product.objects.create(
            name="black pen2",categ=self.category4,price=26.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.product5 = Product.objects.create(
            name="flower",categ=self.category2,price=26.43,compare_price=25.00,
            featured = False,description="abcd"
        )

    def test_get_all_ideas(self):
        
        url = reverse('categories:cat-list')
        response = self.client.get(url)
        # print("response data:", response.data)
        local_serialized_data = CategorySerializer(self.cats, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_serialized_data, response.data)

    def test_get_idea_for_one_category_without_children(self):
        
        # prod-per-categ"
        url = reverse('categories:prod-per-categ', kwargs={"slug": self.category1.slug})
        response = self.client.get(url)
        local_serialized_data = ProductSerializer(self.category1.prods.all(), many=True).data
        count_prods = len(response.data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_serialized_data, response.data) 
        self.assertEqual(1, count_prods)    

    def test_get_idea_for_one_category_with_children(self):
        """return prods own but also prods linked to children categs"""
        url = reverse('categories:prod-per-categ', kwargs={"slug": self.category2.slug})
        response = self.client.get(url)
        count_prods = len(response.data)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(4, count_prods)    