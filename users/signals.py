from django.db.models.signals import post_save
from django.contrib.auth.models import User # sender, sends the signal
from django.dispatch import receiver # receives the signal
from .models import Profile

'''
Matches a profile with a user account
'''

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
