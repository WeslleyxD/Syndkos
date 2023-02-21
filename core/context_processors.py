def user_authenticated(request):
    if request.user.is_authenticated:
        context = {'user_authenticated': request.user}
    else:
        context = {'user_authenticated': 'bem-vindo(a)'}
    
    return context
