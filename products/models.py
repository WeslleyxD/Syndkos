from django.db import models
from core.utils import path_media
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(('Criado em'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(('Modificado em'), auto_now=True)
    slug = models.SlugField(max_length=200)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created_at',)

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='Categoria')
    name = models.CharField(verbose_name=('Nome'), max_length=100)
    description = models.TextField(('Descrição'))
    image = models.ImageField(verbose_name=('Imagem'), upload_to=path_media())
    value = models.DecimalField(('Valor'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(('Criado em'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(('Modificado em'), auto_now=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)