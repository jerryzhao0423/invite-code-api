from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid


class Invitation(models.Model):
    username = models.OneToOneField(User, related_name='invitation', on_delete=models.CASCADE)
    credit = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    invite_code = models.CharField(max_length=36)
    invite_input = models.CharField(max_length=36, blank=True)
    is_invited = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username + 'code'


def create_invitation(sender, instance, created, **kwargs):
    if created:
        Invitation.objects.create(username=instance, invite_code=uuid.uuid1())


post_save.connect(create_invitation, sender=User)
