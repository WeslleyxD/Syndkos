from django.shortcuts import render
from accounts.forms import UserForm
from products.models import Category


def index(request):

  permission_vendedor = request.user.groups.filter(name='Vendedor').exists()
  return render(request, 
                'index.html',
                {
                  'permission_vendedor': permission_vendedor,
                }
  )