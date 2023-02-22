from django.db import models
from products.models import Product
from decimal import Decimal
from accounts.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Usuário')
    address = models.CharField('Endereço', max_length=300)
    email = models.EmailField('E-mail',)
    cep = models.CharField('CEP', max_length=8)
    finish = models.BooleanField('Finalizado', default=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, editable=False)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Pedidos"
        
    def __str__(self):
        return f"{self.address} {self.cep} {self.email}"

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name='Pedido')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='Produto')
    value = models.DecimalField('Valor' ,max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Quantidade', default=1)

    class Meta:
        ordering = ('-order',)
        verbose_name_plural = "Items do pedido"

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity