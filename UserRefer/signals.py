from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Invitation


@receiver(post_save, sender=User)
def init_new_user(sender, instance=None, created=False, **kwargs):
    print(instance)
    if created:
        Invitation.objects.create(username=instance)
