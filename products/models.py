from django.db import models
from core.utils import path_media
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(('Criado em'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(('Modificado em'), auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)
    

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='Categoria', db_index=True)
    name = models.CharField(verbose_name=('Nome'), max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(('Descrição'))
    image = models.ImageField(verbose_name=('Imagem'), upload_to=path_media())
    value = models.DecimalField(('Valor'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(('Criado em'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(('Modificado em'), auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:detail_product', args=[self.category.slug, self.slug])