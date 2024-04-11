from django.contrib import admin
from .models import Post, Comment # R imports the post model created

# Register your models here.
admin.site.register(Post) # R gives admin access to posts from the panel
admin.site.register(Comment)