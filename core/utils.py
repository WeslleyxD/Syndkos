from django.core.paginator import Paginator

def path_media():
    return "products/%Y/%m/%d"

def pagination(request, objects: list, per_page: int):
    paginator = Paginator(objects, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj