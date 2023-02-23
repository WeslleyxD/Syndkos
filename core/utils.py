import json
import requests
from django.core.paginator import Paginator

def path_media():
    return "products/%Y/%m/%d"

def pagination(request, objects: list, per_page: int):
    paginator = Paginator(objects, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def via_cep(cep):
    r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    response = json.loads(r.text)

    response = response.get('erro')

    if not response:
        return r.text
    else:
        return False


