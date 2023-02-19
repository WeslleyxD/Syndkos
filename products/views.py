from django.shortcuts import render
from .forms import CategoryForm, ProductForm

# Create your views here.

# TODO: RESTRINGIR VIEW POR GRUPO
def create(request):
    category_form = CategoryForm()
    product_form = ProductForm()

    if request.method == 'POST':
        if 'category_send' in request.POST:
            print ('poaskdaopksd')
            category_form = CategoryForm(data=request.POST)
        elif 'product_send' in request.POST:
            print ('xddd')
            product_form = ProductForm(data=request.POST)

    return render(request, 
                  'products/create.html',
                  {
                    'category_form': category_form,
                    'product_form': product_form,
                  }
    )