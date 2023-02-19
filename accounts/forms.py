from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups_model']
        # widgets = {
        #     'username': forms.HiddenInput(),
        # }

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
    


class LoginForm(forms.Form):
    email = forms.EmailField(
        label=_('E-mail'), max_length=200, required=True, widget=forms.TextInput()
    )
    password = forms.CharField(
        label=_("Senha"), widget=forms.PasswordInput(),
    )

    error_messages = {
        "invalid_login": _(
            "E-mail ou senha incorreto."
        ),
        "invalid_password": _ (
            "Faltou verificar o recaptcha."
        )
        #"inactive": _("This account is inactive."),
    }
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
        # captcha = cleaned_data.get('captcha', """  """{})
        if not authenticate(username=username, password=password):
            raise ValidationError(
                self.error_messages["invalid_login"],
                code="inactive",
            )
        # if not captcha:
        #     raise ValidationError(
        #     self.error_messages["invalid_password"],
        #     code="inactive",
        #     )
        # return cleaned_data
