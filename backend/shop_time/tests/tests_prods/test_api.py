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
            name="A red pen",categ=self.category,price=23.43,compare_price=24.00,
            featured = False,description="abcd"
        )
        self.product2 = Product.objects.create(
            name="A black pen",categ=self.category,price=26.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.product3 = Product.objects.create(
            name="C green pen",categ=self.category,price=16.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.product4 = Product.objects.create(
            name="D yellow pen",categ=self.category,price=10.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.product5 = Product.objects.create(
            name="E gold pen",categ=self.category,price=26.43,compare_price=25.00,
            featured = False,description="abcd"
        )
        self.product6 = Product.objects.create(
            name="Z siver pen",categ=self.category,price=26.43,compare_price=25.00,
            featured = False,description="abcd yellow"
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
# search
    def test_product_list_search(self):
        """ search will find a term in name as well as in description of product"""
        url = reverse('products:products-list')
        response = self.client.get(url,data={'search': 'yellow'})
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product4.id,self.product6.id))
        
        local_ser_data = ProductSerializer(prods,many=True).data        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data) 

# ordering
    def test_product_list_in_order_highest_price_on_top(self):
        """ order product: highest price on top"""
        url = reverse('products:products-list')
        response = self.client.get(url,data={'ordering': '-price'})
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product1.id,self.product2.id,self.product3.id,self.product4.id,
                            self.product5.id,self.product6.id)).order_by("-price")
        local_ser_data = ProductSerializer(prods,many=True).data    
        local_top_price = local_ser_data[0]['price']
        resp_top_price = response.data[0]['price'] 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data)    
        self.assertEqual(local_top_price,resp_top_price,'26.43')  

    def test_product_list_in_order_lowest_price_on_top(self):
        """ order product: lowest price on top"""
        url = reverse('products:products-list')
        response = self.client.get(url,data={'ordering': 'price'})
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product1.id,self.product2.id,self.product3.id,self.product4.id,
                            self.product5.id,self.product6.id)).order_by("price")
        local_ser_data = ProductSerializer(prods,many=True).data    
        local_top_price = local_ser_data[0]['price']
        resp_top_price = response.data[0]['price'] 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data)    
        self.assertEqual(local_top_price,resp_top_price,'10.43')  

    def test_product_list_in_order_name_A_on_top(self):
        """ order product: lowest price on top (admin name should start with a capital letter"""
        url = reverse('products:products-list')
        response = self.client.get(url,data={'ordering': 'name'})
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product1.id,self.product2.id,self.product3.id,self.product4.id,
                            self.product5.id,self.product6.id)).order_by("name")
        local_ser_data = ProductSerializer(prods,many=True).data    
        local_top_name = local_ser_data[0]['name']        
        resp_top_name = response.data[0]['name']       
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data)    
        self.assertEqual(local_top_name,resp_top_name) 

    def test_product_list_in_order_name_Z_on_top(self):    
        """ order product: lowest price on top( admin name should start with a capital letter)"""
        url = reverse('products:products-list')
        response = self.client.get(url,data={'ordering': '-name'})
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product1.id,self.product2.id,self.product3.id,self.product4.id,
                            self.product5.id,self.product6.id)).order_by("-name")
        local_ser_data = ProductSerializer(prods,many=True).data           
        local_top_name = local_ser_data[0]['name']        
        resp_top_name = response.data[0]['name']       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_ser_data,response.data)    
        self.assertEqual(local_top_name,resp_top_name)    
# filter    
    def test_get_filter_one_price(self):
        """ get a list of prods for a given price """
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product2.id,self.product5.id,self.product6.id))
                            
        url = reverse('products:products-list')
        serializer_data = ProductSerializer(prods, many=True).data
        resp = self.client.get(url, data={"price": "26.43"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, resp.data)
        self.assertEqual(len(serializer_data), len(resp.data)) 

    def test_get_filter_range_price(self):
        """ get a list of prods for a given range in price (default order: -date_created"""
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product1.id,self.product2.id,self.product5.id,self.product6.id))
                            
        url = reverse('products:products-list')
        serializer_data = ProductSerializer(prods, many=True).data
        print("ser-data",serializer_data)
        resp = self.client.get(url, data={"min_price": "20.00","max_price":'50.00'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, resp.data)
        self.assertEqual(len(serializer_data), len(resp.data))

    def test_get_filter_range_price(self):
        """ get a list of prods for a given range in price AND order by price (lowers on top)"""
        prods = Product.objects.annotate(
            an_likes = Count(Case(When(userproductrelation__like=True,then=1))),
            avg_rate = Avg('userproductrelation__rating')
            ).filter(id__in=(self.product1.id,self.product2.id,self.product5.id,self.product6.id)).order_by('price')
                            
        url = reverse('products:products-list')
        serializer_data = ProductSerializer(prods, many=True).data
        # print("ser-data",serializer_data)
        resp = self.client.get(url, data={"min_price": "20.00","max_price":'50.00',"ordering":"price"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, resp.data)
        self.assertEqual(len(serializer_data), len(resp.data))       
      
