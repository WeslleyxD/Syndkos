from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # path('create/', views.create, name='create'),
    path('manager/', views.manager, name='manager'),

    #category
    path('manager/category/', views.list_category, name='list_category'),
    path('manager/category/create', views.create_category, name='create_category'),
    path('manager/category/update/<int:id>/', views.update_category, name='update_category'),
    path('manager/category/delete/<int:id>/', views.delete_category, name='delete_category'),

    #product
    path('manager/product/', views.list_product, name='list_product'),
    path('manager/product/create', views.create_product, name='create_product'),
    path('manager/product/update/<int:id>/', views.update_product, name='update_product'),
    path('manager/product/delete/<int:id>/', views.delete_product, name='delete_product'),


]