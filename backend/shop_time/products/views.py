from django.db.models import When, Case, Count, Avg
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend   # installed app dj_filters
       
from django_filters import rest_framework as dj_filters         # installed app dj_filters

from rest_framework.filters import SearchFilter, OrderingFilter                             

from .models import Product
from serializers.prods.prod_ser import ProductSerializer

class ProductFilter(dj_filters.FilterSet):
    name = dj_filters.CharFilter(lookup_expr='icontains')
    price = dj_filters.NumberFilter()
    min_price = dj_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = dj_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ('price', 'min_price','max_price','in_stock','name','categ')
    

class ProductRetrListViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    """get single prod object and list of products (default ordering ascend price('- price'))"""
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = (SearchFilter,OrderingFilter,DjangoFilterBackend,)
    # djano_filter
    filterset_class = ProductFilter
    # built-in 
    search_fields = ['name','price','categ__name','description'] # default ?search=cat (charField,textField)
    ordering_fields = ['price','name']

    
    def get_queryset(self):
        queryset = Product.objects.annotate(
            an_likes=Count(Case(When(userproductrelation__like=True, then=1))),
            avg_rate=Avg('userproductrelation__rating'),
            )
        # sqlite dictinct(raise NotSupportedError('DISTINCT ON fields is not supported by this database backend'))
        
        return queryset    

    
