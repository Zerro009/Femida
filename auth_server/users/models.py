from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length=32,
        unique=True, 
        verbose_name='Логин',
    )
    email = models.EmailField(
        verbose_name='Почта',
    )
    password = models.CharField(
        max_length=2048,
        verbose_name='Пароль',
    )
