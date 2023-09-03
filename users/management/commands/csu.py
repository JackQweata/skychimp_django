from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from main.models import MailingSettings, MailingAttempt
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admin@sky.pro',
            full_name='Admin Root',
            is_staff=True,
            is_superuser=True
        )

        admin.set_password('123')
        admin.save()

        manager = User.objects.create(
            email='manager@sky.pro',
            full_name='Manager Root',
            is_staff=True
        )

        group, create = Group.objects.get_or_create(name='manager')

        setting = ContentType.objects.get_for_model(MailingSettings)
        malling = ContentType.objects.get_for_model(MailingAttempt)
        user = ContentType.objects.get_for_model(User)

        perm_change_settings = Permission.objects.get(codename='change_mailingsettings', content_type=setting)
        perm_view_malling = Permission.objects.get(codename='view_mailingattempt', content_type=malling)
        perm_change_user = Permission.objects.get(codename='change_user', content_type=user)
        perm_view_user = Permission.objects.get(codename='view_user', content_type=user)

        group.permissions.add(
            perm_change_settings,
            perm_change_user,
            perm_view_user,
            perm_view_malling
        )

        manager.groups.add(group)
        manager.set_password('123')
        manager.save()
