# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='profile/', verbose_name='عکس پروفایل', null=True, blank=True)
