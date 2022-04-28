from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db import models
from django.utils import timezone

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=64, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64, blank=True)

    avatar = models.ImageField(verbose_name='Аватар', blank=True)
    description = models.TextField(verbose_name='Описание профиля', blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
