from django.db import models
from core.utils import path_media

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=path_media())
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name