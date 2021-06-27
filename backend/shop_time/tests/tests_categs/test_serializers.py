from django.test import TestCase
from categories.models import Category
from serializers.categs.serializers import CategorySerializer


class CategoryListTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="fizz")
        self.category2 = Category.objects.create(name="abcd")
        self.category3 = Category.objects.create(name="fizzbazzz", parent=self.category2)
        self.category4 = Category.objects.create(name="zzz", parent=self.category3)
        self.category5 = Category.objects.create(name="mio")

        self.categs = Category.objects.all()

    def test_one_categ_children(self):
        """ check whether all children are included for 1 category"""
        ser_data = CategorySerializer(self.category2).data
        expected_data = {
            "id": self.category2.id, "name": "abcd",
            "slug": "abcd", "children": [
                {"id": self.category3.id,
                 "name": "fizzbazzz",
                 "slug": "fizzbazzz",
                 "children": [
                     {"id": self.category4.id,
                      "name": "zzz",
                      "slug": "zzz",
                      "children": []
                      }
                 ]
                 }
            ]
        }
        self.assertEqual(ser_data, expected_data)    

    def test_check_categ_roots(self):
        """categories to render on front should be only roots(parents=None)"""
        categs = CategorySerializer(self.categs, many=True).data
        self.assertEqual(len(categs), 3)    
       
