from django.shortcuts import render
from django.views import generic
from .models import Post

class PostEntries(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6