from django.db import models
from products.models import Product
from decimal import Decimal
from accounts.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=300)
    email = models.EmailField()
    cep = models.CharField(max_length=8)
    finish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return f"{self.address} {self.cep} {self.email}"

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,  related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity