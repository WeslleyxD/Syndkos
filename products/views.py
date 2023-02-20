from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, ProductForm
from .models import Category, Product
from django.contrib.auth.decorators import permission_required
from django.forms import modelform_factory
import json
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

# # TODO: RESTRINGIR VIEW POR GRUPO
# @permission_required('products.add_product', raise_exception=True)
# def create(request):

#     print (request.user)
#     category_form = CategoryForm()
#     product_form = ProductForm()

#     # print (request.user.get_group_permissions())

#     if request.method == 'POST':
#         if 'category_send' in request.POST:
#             print ('poaskdaopksd')
#             category_form = CategoryForm(data=request.POST)
#         elif 'product_send' in request.POST:
#             print ('xddd')
#             product_form = ProductForm(data=request.POST)

#     return render(request, 
#                   'products/create.html',
#                   {
#                     'category_form': category_form,
#                     'product_form': product_form,
#                   }
#     )

@permission_required('products.add_product', raise_exception=True)
def manager(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'products/manager.html',
                  {
                    'categories': categories,
                    'products': products
                  })

@permission_required('products.add_product', raise_exception=True)
def list_category(request):
    categories = Category.objects.all()

    return render(request, 'products/list_category.html',
                  {
                    'categories': categories,
                  })

@permission_required('products.add_product', raise_exception=True)
def create_category(request):
    category_form = CategoryForm()

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect ('products:list_category')
        
        return render(request, 'products/create_category.html', {'category_form': category_form})
    
    return render(request, 'products/create_category.html', {'category_form': category_form})
  
@permission_required('products.add_product', raise_exception=True)
def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    category_form = CategoryForm(instance=category)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect ('products:list_category')
        
        return render(request, 'products/update_category.html',{'category_form': category_form,})

    return render(request, 'products/update_category.html',{'category_form': category_form,})

@permission_required('products.add_product', raise_exception=True)
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect ('products:list_category')

    return render(request, 'products/delete_category.html', {'category': category})






#PRODUCTS
@permission_required('products.add_product', raise_exception=True)
def list_product(request):
    products = Product.objects.all()

    return render(request, 'products/list_product.html',
                  {
                    'products': products,
                  })


@permission_required('products.add_product', raise_exception=True)
def create_product(request):
    product_form = ProductForm()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect ('products:list_product')

        return render(request, 'products/create_product.html', {'product_form': product_form})

    return render(request, 'products/create_product.html', {'product_form': product_form})

@permission_required('products.add_product', raise_exception=True)
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    product_form = ProductForm(instance=product)

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect ('products:list_product')

        return render(request, 'products/update_product.html', {'product_form': product_form,})
    
    return render(request, 'products/update_product.html', {'product_form': product_form,})

@permission_required('products.add_product', raise_exception=True)
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect ('products:list_product')

    return render(request, 'products/delete_product.html', {'product': product})