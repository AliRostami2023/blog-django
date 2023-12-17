from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name='full name')
    about_us = models.TextField(max_length=1000, verbose_name='about us', null=True, blank=True)
    email_active_code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

