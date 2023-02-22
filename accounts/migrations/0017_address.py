# Generated by Django 4.1.7 on 2023-02-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_user_address_remove_user_cep_remove_user_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('state', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal')], max_length=200, null=True, verbose_name='Estado')),
                ('city', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('address', models.CharField(blank=True, max_length=254, null=True, verbose_name='Logradouro')),
                ('number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=254, null=True, verbose_name='Complemento')),
            ],
        ),
    ]