# from django.shortcuts import redirect
# from django.urls import reverse
# from django.http import HttpResponseRedirect

# class RestrictAppMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             # Verifica se o usuário tem permissão de acesso ao aplicativo
#             if not request.user.groups.filter(name='grupo_com_permissao').exists():
#                 # Redireciona para página de acesso negado
#                 return HttpResponseRedirect(reverse('core:index'))

#         response = self.get_response(request)

#         return response
