from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

GROUPS = [
    ('CLIENTE', 'Cliente'),
    ('VENDEDOR', 'Vendedor'),
]

STATES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('DF', 'Distrito Federal'),
]


class Address(models.Model):
    cep = models.CharField('CEP', max_length=8, null=True, blank=True)
    state = models.CharField('Estado', max_length=200, null=True, blank=True, choices=STATES)
    city = models.CharField('Cidade', max_length=20, null=True, blank=True)
    district = models.CharField('Bairro', max_length=100, null=True, blank=True)
    address = models.CharField('Logradouro', max_length=254, null=True, blank=True)
    number = models.CharField('Número', max_length=10, null=True, blank=True)
    complement = models.CharField('Complemento', max_length=254, null=True, blank=True)
    selected = models.BooleanField('Selecionado', default=False)

    class Meta:
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.get_full_address()
    
    def get_full_address(self):
        return f"{self.state} {self.city} {self.district} {self.address} {self.number} {self.complement}"

class User(AbstractUser):
    address = models.ManyToManyField(Address, related_name='users', verbose_name='Endereços')
    username = models.CharField('Usuário',max_length=15, unique=True)
    email = models.EmailField('E-mail', unique=True)
    groups_model = models.CharField('Grupo', max_length=10, choices=GROUPS, default='Cliente')
    first_name = models.CharField("Nome", max_length=150)
    last_name = models.CharField("Sobrenome", max_length=150)

    def __str__(self):
        return self.username
