from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models import When, Case, Count, Avg

from categories.models import Category
from products.models import Product,UserProductRelation

from serializers.prods.prod_ser_test import ProductTestSerializer

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
                

    def test_product_serializer(self):
        """ """
        ser_data = ProductTestSerializer(self.prods,many=True).data        
        expected_data = [
            {
            "id":self.product1.id,"name": "red pen","categ": self.category.id, "categ_name":self.category.name,
            "slug": "red-pen","price":'23.43',"compare_price":'24.00',"discount":'0.00',"featured":False,
            "description":"abcd","an_likes":1,"avg_rate":'5.00',"sold":0
            },
            {
            "id":self.product2.id,"categ": self.category.id, "categ_name":self.category.name,"name": "black pen",
            "slug": "black-pen","price":'26.43',"compare_price":'25.00',"discount":'0.00',"featured":False,
            "description":"abcd","an_likes":0,"avg_rate":'4.00',"sold":0
            },
        ]        
        self.assertEqual(ser_data, expected_data)    

        
      