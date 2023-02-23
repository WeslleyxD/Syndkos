from django.core.management.base import BaseCommand, CommandError
# from accounts.models import User
from django.apps import apps
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    
    def handle(self, *args, **options):
        super().handle(*args, **options)
        all_models = apps.get_models()


        create_group_seller = Group.objects.update_or_create(name='Cliente')
        create_group_seller = Group.objects.update_or_create(name='Vendedor')
        

        # my_group.permissions.add(permission)

        group_client = Group.objects.get(name='Cliente')
        group_seller = Group.objects.get(name='Vendedor')

        perms = Permission.objects.all()
        for perm in perms:
            if perm.content_type.model in ['category', 'product']:
                group_seller.permissions.add(perm)


        self.stdout.write(self.style.SUCCESS('Data initialized successfully!'))