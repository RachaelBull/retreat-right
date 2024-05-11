from django.db import models
from django.contrib.auth.models import User


class UsersPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, default="")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'
