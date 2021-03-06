from django.db import models
from django.contrib.auth.models import AbstractUser
from django.views.decorators.http import require_safe

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')