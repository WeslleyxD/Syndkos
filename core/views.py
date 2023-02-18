from django.shortcuts import render
from accounts.forms import UserForm


def index(request):
    user_form = UserForm()
    print (user_form)
    return render(request, 
                  'index.html',
                  {
                    'user_form': user_form,
                  }
    )