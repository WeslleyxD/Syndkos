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
        exclude = ['selected', 'user']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups_model', 'first_name', 'last_name', ]
        help_texts = {
            'cep': ('Preencha o cep'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user
    
    def clean(self):
        cleaned_data = super().clean()
        cep = cleaned_data.get("cep", "")

        if not cep.isnumeric() or len(cep.strip()) < 8:
            self.add_error('cep', 'Insira o cep apenas com números')



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




# class AddresSelectForm(forms.Form):
#     products = forms.ModelChoiceField(
#         queryset=None,
#         widget=forms.CheckboxSelectMultiple,
#     )

#     class Meta:
#         model = Address
#         fields = '__all__'

#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         address = user.address.all()
#         self.fields['products'].queryset = address

#         my_field_value = self.fields['products']

#         print (my_field_value.initial)
#         print (dir(my_field_value))
        # address = user1.__class__.objects.all()

        # self.fields['products'].queryset = address
