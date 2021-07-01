from django.urls import path
from .views import CategoryListView,ProductsPerCategListView

app_name = 'categories'

urlpatterns = [
    # just as a sandBox; cach will last for 60seconds
    # path('', cache_page(60)(CategoryList.as_view()),name='list'),
    path('', CategoryListView.as_view(), name='cat-list'),
    path('<slug>/', ProductsPerCategListView.as_view(), name="prod-per-categ"),
    


]