from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase


User = get_user_model()


class UserCreateDjoserSerializerTesCase(APITestCase):
    """return user info for djoser url='auth/users/me' redirect"""
   
    def setUp(self):
        self.user = User.objects.create(first_name="jane",last_name="Frost", email="zoo@mail.com")

    def test_get_user(self):
        """ via djoser built-in view: get user attr"""
        self.client.force_authenticate(user=self.user)
        url = '/auth/users/me'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)
        