from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cpf  = models.CharField(max_length=11)
    foto = models.ImageField(blank= True)