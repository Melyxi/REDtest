from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            email = ''
        else:
            email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):  # создаем суперпользователя с ролью разработчика
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'DEV')

        if extra_fields.get('role') is not 'DEV':
            raise ValueError('Superuser must have is_superuser="DEV"')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    ADMIN = 'ADMIN'
    USER = 'USER'
    DEVELOPER = "DEV"

    ROLE_CHOICES = (
        (ADMIN, 'Administrator'),
        (USER, 'User'),
        (DEVELOPER, 'Developer')
    )
    role = models.CharField(choices=ROLE_CHOICES, default=USER, blank=True, null=True, max_length=50)
    objects = UserManager()

    def save(self, *args, **kwargs):

        if self.role == "DEV":
            self.is_superuser = True
            return super(self.__class__, self).save()
        else:
            self.is_superuser = False
            return super(self.__class__, self).save()
