from products.models import Category

def categories(request):
    categories = {}

    categories.update({'categories_slice': Category.objects.all()[0:4]})
    categories.update({'categories': Category.objects.all()[4:]})

    return categories