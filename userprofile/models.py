from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userspage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='nobody.jpg', upload_to='user_pics')
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.name} Profile'