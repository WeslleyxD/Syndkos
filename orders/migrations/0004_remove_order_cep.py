# Generated by Django 4.1.7 on 2023-02-22 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_address_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cep',
        ),
    ]
