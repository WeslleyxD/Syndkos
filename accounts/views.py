from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            # return redirect('core:index')


    return render(request, 
                  'accounts/register.html',
                  {
                    'user_form': user_form,
                  }
    )

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

                return redirect ('core:index')

    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')