from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UsersPage(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, default="")
    bio = models.TextField()

    def __str__(self):
        return f'{self.name}'