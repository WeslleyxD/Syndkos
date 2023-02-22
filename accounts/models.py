from django.db import models
from django.contrib.auth.models import AbstractUser

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


class User(AbstractUser):
    username = models.CharField('Usuário',max_length=15, unique=True)
    email = models.EmailField('E-mail', unique=True)
    groups_model = models.CharField('Grupo', max_length=10, choices=GROUPS, default='Cliente')
    first_name = models.CharField("Nome", max_length=150)
    last_name = models.CharField("Sobrenome", max_length=150)

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='Adresses', verbose_name='Usuários', null=True, blank=True)
    cep = models.CharField('CEP', max_length=8)
    state = models.CharField('Estado', max_length=200, choices=STATES)
    city = models.CharField('Cidade', max_length=20)
    district = models.CharField('Bairro', max_length=100)
    address = models.CharField('Logradouro', max_length=254)
    number = models.CharField('Número', max_length=10)
    complement = models.CharField('Complemento', max_length=254, blank=True)
    selected = models.BooleanField('Selecionado', default=False)

    class Meta:
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.get_full_address()
    
    def get_full_address(self):
        return f"{self.cep} {self.state} {self.city} {self.district} {self.address} {self.number} {self.complement}"
