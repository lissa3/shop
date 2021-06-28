from django.urls import path,include
from rest_framework import routers
from .views import ProductRetrListViewSet

app_name = 'products'

router = routers.SimpleRouter()
router.register(r'product', ProductRetrListViewSet,basename="products")

urlpatterns = router.urls

urlpatterns = [
    path('products/',include(router.urls)),
    


]