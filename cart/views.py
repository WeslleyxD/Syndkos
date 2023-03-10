from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartUpdateProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartUpdateProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_detail')

def cart_detail(request):
    if not request.user.is_authenticated:
        return render(request, 'cart/not_login.html')

    cart = Cart(request)

    for item in cart:
        print (item)
        item['add_quantity_form'] = CartAddProductForm()
        item['update_quantity_form'] = CartUpdateProductForm()

    return render(request, 'cart/detail_cart.html', {'cart': cart})