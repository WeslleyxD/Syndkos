from django.db import models
from core.utils import path_media

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(('Criado em'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(('Modificado em'), auto_now=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='Categoria')
    name = models.CharField(verbose_name=('Nome'), max_length=100)
    description = models.TextField(('Descrição'))
    image = models.ImageField(verbose_name=('Imagem'), upload_to=path_media())
    value = models.DecimalField(('Valor'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(('Criado em'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(('Modificado em'), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)