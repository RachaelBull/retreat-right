from . import views
from django.urls import path

urlpatterns = [
    path('profile', views.UserProfile.as_view(), name='profile'),
    #path('', views.users_page, name='userprofile'),
]