import uuid
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length = 12, unique = True)
    is_phone_verified = models.BooleanField(default = False)
    otp = models.CharField(max_length = 6)
    username = models.CharField(max_length = 14, unique = True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()