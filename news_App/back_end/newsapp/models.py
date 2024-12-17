from django.db import models
# django.core import validators as v
from django.contrib.auth.models import AbstractUser

class NewsUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
