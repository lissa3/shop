from django.shortcuts import get_object_or_404
from django.db.models import Q
import operator 
from functools import reduce

from .models import Category
from products.models import Product
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from serializers.categs.serializers import CategorySerializer
from serializers.prods.prod_ser import ProductSerializer

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    pagination_class= None
    queryset = Category.objects.all()



def get_queryset_descendants(nodes, include_self=False):
        filters = [] 
        for n in nodes: 
            lft, rght = n.lft, n.rght 
            if include_self:
                lft -=1 
                rght += 1 
            filters.append(Q(tree_id=n.tree_id, lft__gt=lft, rght__lt=rght)) 
        print("filter",filter)    
        q = reduce(operator.or_, filters) 
        return Category.tree.filter(q)    

class ProductsPerCategListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        categ = get_object_or_404(Category,slug=slug)
        if categ.children:
            categs_desc = categ.get_descendants(include_self=True)
            queryset = Product.objects.filter(categ__in=categs_desc) 
            print("found some desc; amount: ",queryset.count())     
        else:
            queryset = Product.objects.filter(categ=categ)
            print("desc not found ")     
        return queryset






