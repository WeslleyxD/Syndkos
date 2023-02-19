from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

GROUPS = [
    ('CLIENTE', 'Cliente'),
    ('VENDEDOR', 'Vendedor'),
]

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    groups_model = models.CharField(verbose_name='Grupo', max_length=10, choices=GROUPS, default='Cliente')
