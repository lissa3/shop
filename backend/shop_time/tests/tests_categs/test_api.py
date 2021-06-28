from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import  Category
from serializers.categs.serializers import CategorySerializer



User = get_user_model()


class CategTestCase(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="chat")
        self.category2 = Category.objects.create(name="kletskoek")
        self.category3 = Category.objects.create(name="talk", parent=self.category2)
        self.category4 = Category.objects.create(name="ha-ha", parent=self.category3)
        self.category5 = Category.objects.create(name="zoo", parent=self.category4)       
        self.cats = Category.objects.all()

    def test_get_all_ideas(self):
        url = reverse('categories:cat-list')
        response = self.client.get(url)
        # print("response data:", response.data)
        local_serialized_data = CategorySerializer(self.cats, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_serialized_data, response.data)