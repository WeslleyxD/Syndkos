from orders.models import Order
from products.forms import CategoryForm, ProductForm
from products.models import Category, Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('products.add_product', raise_exception=True)
def manager(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'manager/manager.html', {'categories': categories,'products': products})


@permission_required('products.add_product', raise_exception=True)
def list_category(request):
    categories = Category.objects.all()

    return render(request, 'manager/list_category.html', {'categories': categories,})


@permission_required('products.add_product', raise_exception=True)
def create_category(request):
    category_form = CategoryForm()

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect ('manager:list_category')
        
        return render(request, 'manager/create_category.html', {'category_form': category_form})
    
    return render(request, 'manager/create_category.html', {'category_form': category_form})
  

@permission_required('products.add_product', raise_exception=True)
def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    category_form = CategoryForm(instance=category)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect ('manager:list_category')
        
        return render(request, 'manager/update_category.html',{'category_form': category_form,})

    return render(request, 'manager/update_category.html',{'category_form': category_form,})


@permission_required('products.add_product', raise_exception=True)
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect ('manager:list_category')

    return render(request, 'manager/delete_category.html', {'category': category})



#PRODUCTS
@permission_required('products.add_product', raise_exception=True)
def list_product(request):
    products = Product.objects.all()

    return render(request, 'manager/list_product.html', {'products': products,})


@permission_required('products.add_product', raise_exception=True)
def create_product(request):
    product_form = ProductForm()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect ('manager:list_product')

        return render(request, 'manager/create_product.html', {'product_form': product_form})

    return render(request, 'manager/create_product.html', {'product_form': product_form})


@permission_required('products.add_product', raise_exception=True)
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    product_form = ProductForm(instance=product)

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect ('manager:list_product')

        return render(request, 'manager/update_product.html', {'product_form': product_form,})
    
    return render(request, 'manager/update_product.html', {'product_form': product_form,})


@permission_required('products.add_product', raise_exception=True)
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect ('manager:list_product')

    return render(request, 'manager/delete_product.html', {'product': product})



#ORDERS
@permission_required('products.add_product', raise_exception=True)
def list_order(request):
    orders = Order.objects.all()
    print (orders)

    return render(request, 'manager/list_order.html', {'orders': orders,})
