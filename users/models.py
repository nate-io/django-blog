from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image_dir = 'profile_pics'
  image = models.ImageField(default=f'/{image_dir}/default.jpg', upload_to=image_dir)

  def __str__(self):
    return f'{self.user.username} Profile'