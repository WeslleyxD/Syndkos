# Generated by Django 4.1.7 on 2023-02-22 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='complement',
        ),
        migrations.RemoveField(
            model_name='user',
            name='district',
        ),
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=15, unique=True, verbose_name='Usuário'),
        ),
    ]
