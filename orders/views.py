from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# def create_order(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         print (dir(request.user))
#         # print (request.user.address)
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order,
#                                         product=item['product'],
#                                         value=item['value'],
#                                         quantity=item['quantity'])
#             # clear the cart
#             cart.clear()
#             return render(request, 'orders/create_order.html', {'order': order})
#     else:
#         form = OrderCreateForm()

#     return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})

def create_order(request):
    cart = Cart(request)
    # select_address = AddresSelectForm(user=request.user)
    if request.method == 'POST':
        order_create = OrderCreateForm(request.POST)
        if order_create.is_valid():
            order = order_create.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        value=item['value'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'orders/create_order.html', {'order_create': order_create})
    else:
        order_create = OrderCreateForm()

    return render(request, 'orders/create_order.html', {'cart': cart, 'order_create': order_create})