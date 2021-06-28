from django.db.models import When, Case, Count, Avg
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import AllowAny

from .models import Product
from serializers.prods.prod_ser import ProductSerializer

class ProductRetrListViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    
    def get_queryset(self):
        queryset = Product.objects.annotate(
            an_likes=Count(Case(When(userproductrelation__like=True, then=1))),
            avg_rate=Avg('userproductrelation__rating'),
            )
        # sqlite dictinct(raise NotSupportedError('DISTINCT ON fields is not supported by this database backend'))
        
        return queryset    

    
