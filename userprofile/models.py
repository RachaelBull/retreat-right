from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userspage(models.Model):
    nickname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)