from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cpf  = models.CharField(max_length=11)
    foto = models.ImageField(upload_to='user_foto', verbose_name='Foto', null=True, blank=True)