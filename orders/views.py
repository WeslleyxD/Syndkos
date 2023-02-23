from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages
from accounts.forms import AddressForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    address_form = AddressForm()
    cart = Cart(request)
    if cart.get_quantity_products() == 0:
        messages.warning(request, 'Para criar um pedido precisa antes preencher o carrinho')
        return redirect('cart:cart_detail')
    if request.method == 'POST':
        print (request.POST)
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save()
            order = Order.objects.create(user=request.user, address=address, email=request.user.email)

            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        value=item['value'],
                                        quantity=item['quantity'])
            cart.clean()
            return redirect('accounts:list_order')

        return render(request, 'accounts/register.html', {'address_form': address_form})

    return render(request, 'orders/create_order.html', {'cart': cart, 'address_form': address_form})