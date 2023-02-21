from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from core.utils import pagination


def select_category(request):
    return render(request, 'products/select_category.html')

def list_products(request, category_slug=None):
    category = None
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    page_obj = pagination(request, products, 3)

    return render(request, 
                'products/list_products.html',
                {'category': category,
                'page_obj': page_obj,
            })