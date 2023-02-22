from .models import Address
from .forms import UserForm, LoginForm, AddressForm
from orders.models import Order
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    user_form = UserForm()    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:login_user')

    return render(request, 'accounts/register.html',{'user_form': user_form,})

def login_user(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                if user.groups.filter(name='Vendedor').exists():
                    return redirect('manager:manager')
                if 'next' in request.META['HTTP_REFERER']:
                    return redirect(request.META['HTTP_REFERER'].split('next=')[1])

                return redirect ('accounts:home')

    return render(request, 'accounts/login.html', {'login_form': login_form})


def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')


@login_required
def home(request):
    return render(request, 'accounts/home.html')


@login_required()
def list_address(request):
    address = Address.objects.filter(user=request.user)
    return render(request, 'accounts/list_address.html', {'address': address})


@login_required()
def create_address(request):
    address_form = AddressForm()

    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address_form.save(user=request.user)

            return redirect ('accounts:list_address')
        
        return render(request, 'accounts/create_address.html', {'address_form': address_form})
    
    return render(request, 'accounts/create_address.html', {'address_form': address_form})


@login_required
def update_address(request, id):
    address = get_object_or_404(Address, id=id)
    address_form = AddressForm(instance=address)

    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=address)
        if address_form.is_valid():
            address_form.save()
            return redirect ('accounts:list_address')

        return render(request, 'accounts/update_address.html', {'address_form': address_form,})
    
    return render(request, 'accounts/update_address.html', {'address_form': address_form,})


@login_required
def delete_address(request, id):
    address = get_object_or_404(Address, id=id)

    if request.method == 'POST':
        address = get_object_or_404(Address, id=id)
        address.delete()
        return redirect ('accounts:list_address')

    return render(request, 'accounts/delete_address.html', {'address': address})


@login_required
def list_order(request):
    order = Order.objects.filter(user=request.user)
    return render(request, 'accounts/list_order.html', {'orders': order})