from .models import Category
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from serializers.categs.serializers import CategorySerializer

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    pagination_class= None
    queryset = Category.objects.all()
