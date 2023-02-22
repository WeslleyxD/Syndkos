from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),

    #Address
    path('address/', views.list_address, name='list_address'),
    path('address/create', views.create_address, name='create_address'),
    path('address/update/<int:id>/', views.update_address, name='update_address'),
    path('address/delete/<int:id>/', views.delete_address, name='delete_address'),

    #Order
    path('order/', views.list_order, name='list_order'),
]