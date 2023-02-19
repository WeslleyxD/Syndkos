from .models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete

# @receiver(pre_save, sender=User)
# def generator_username(sender, instance, created, **kwargs):


@receiver(post_save, sender=User)
def manage_permissions(sender, instance, created, **kwargs):

    group_instance = instance.groups_model.title()
    group = Group.objects.get(name=group_instance)
    if created:
        instance.groups.add(group)
