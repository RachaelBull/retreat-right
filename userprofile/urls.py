from . import views
from django.urls import path

urlpatterns = [
    path('', views.users_page, name='userprofile'),
]