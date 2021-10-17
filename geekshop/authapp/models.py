from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar_media', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
