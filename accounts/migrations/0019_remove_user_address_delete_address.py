# Generated by Django 4.1.7 on 2023-02-22 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_address_options_address_selected_user_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
