from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# Create a new Profile attached to a User upon user creation
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

# Update Profile on User update
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  instance.profile.save()
