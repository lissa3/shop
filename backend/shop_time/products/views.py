from django.db.models import When, Case, Count, Avg
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Product
from serializers.prods.prod_ser import ProductSerializer

class ProductRetrListViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    """get single prod object and list of products (default ordering ascend price('- price'))"""
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    filterset_fields = ['price', 'in_stock','name','categ']

    search_fields = ['name','price','categ__name'] # default ?search=cat (charField,textField)

    ordering_fields = ['price','name','in_stock']

    
    def get_queryset(self):
        queryset = Product.objects.annotate(
            an_likes=Count(Case(When(userproductrelation__like=True, then=1))),
            avg_rate=Avg('userproductrelation__rating'),
            )
        # sqlite dictinct(raise NotSupportedError('DISTINCT ON fields is not supported by this database backend'))
        
        return queryset    

    
