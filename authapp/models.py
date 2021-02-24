from django.db import models
#
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'ADMIN'
    USER = 'USER'

    ROLE_CHOICES = (
        (ADMIN, 'Administrator'),
        (USER, 'User'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default=USER, blank=True, null=True, max_length=50)