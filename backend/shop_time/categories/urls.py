from django.urls import path
from .views import CategoryListView

app_name = 'categories'

urlpatterns = [
    # just as a sandBox; cach will last for 60seconds
    # path('', cache_page(60)(CategoryList.as_view()),name='list'),
    path('', CategoryListView.as_view(), name='cat-list'),
    


]