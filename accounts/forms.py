from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.utils import via_cep

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups_model', 'first_name', 'last_name', 'cep', 'state', 'city', 'district', 'address', 'number', 'complement']
        help_texts = {
            'cep': ('Preencha o cep'),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].initial = str(uuid4())

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

    # error_messages = {
    #     "invalid_login": _(
    #         "E-mail ou senha incorreto."
    #     ),
    #     "invalid_password": _ (
    #         "Faltou verificar o recaptcha."
    #     )
        #"inactive": _("This account is inactive."),
    # }
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get("username")
    #     password = cleaned_data.get("password")
    #     if User.objects.filter(username__iexact=username):
    #         ok = User.objects.get(username__iexact=username)
    #         print (dir(ok))
    #         print (ok.set_password)
    #         msg = "Usuário ou senha incorreto"
    #         self.add_error('username', msg)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if not authenticate(username=username, password=password):
            self.add_error('email', 'E-mail ou senha incorreto')
