from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def the_blog(request):
    return HttpResponse("This is my blog test message")