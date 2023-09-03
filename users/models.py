from django.contrib.auth.models import AbstractUser
from django.db import models

BLANCNULL = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(**BLANCNULL, verbose_name='Комментарий')
    token_reg = models.CharField(max_length=100, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
