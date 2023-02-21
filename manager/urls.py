from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    # path('create/', views.create, name='create'),
    path('', views.manager, name='manager'),

    #category
    path('category/', views.list_category, name='list_category'),
    path('category/create', views.create_category, name='create_category'),
    path('category/update/<int:id>/', views.update_category, name='update_category'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),

    #product
    path('product/', views.list_product, name='list_product'),
    path('product/create', views.create_product, name='create_product'),
    path('product/update/<int:id>/', views.update_product, name='update_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),


]