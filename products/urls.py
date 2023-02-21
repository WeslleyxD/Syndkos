from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.select_category, name='select_category'),
    path('<str:category_slug>/', views.list_products, name='product_list_by_category'),
    path('search', views.search_list_products, name="search_list_products"),
]