from django import forms
from .models import User, Address
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.utils import via_cep
from django.forms import inlineformset_factory


class AddressForm(forms.ModelForm):
    class Meta: 
        model = Address
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True, user=None):
        address = super().save(commit=False)
        
        if user:
            address.user = user
        if commit:
            address.save()
        return address
    
    def clean(self):
        cleaned_data = super().clean()
        cep = cleaned_data.get("cep", '')
        print (cep)
        
        if not cep.isnumeric() or len(cep.strip()) < 8:
            print (3)
            self.add_error('cep', 'Cep inválido')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups_model', 'first_name', 'last_name', ]

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        label=_('E-mail'), max_length=200, required=True, widget=forms.TextInput()
    )
    password = forms.CharField(
        label=_("Senha"), widget=forms.PasswordInput(), required=True,
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if not authenticate(username=username, password=password):
            self.add_error('email', 'E-mail ou senha incorreto')