from .models import Product, Category
from cart.forms import CartAddProductForm
from core.utils import pagination
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST


def select_category(request, search_products):
    return render(request, 'products/select_category.html')

def list_products(request, category_slug=None):
    category = None
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    page_obj = pagination(request, products, 3)

    return render(request, 'products/list_products.html', {'category': category,'page_obj': page_obj,})


def search_list_products(request):
    search = ''
    if request.method == 'POST':
        search = request.POST['search']

    products = Product.objects.filter(Q(name__icontains=search) | Q(category__name__icontains=search))

    page_obj = pagination(request, products, 3)

    return render(request, 'products/search_list_products.html', {'page_obj': page_obj})



def detail_product(request, category_name, slug):
    #Produto selecionado no template list products
    product = get_object_or_404(Product, slug__iexact=slug)

    cart_product_form = CartAddProductForm()

    return render(request, 'products/detail_product.html', {'product': product, 'cart_product_form': cart_product_form,})