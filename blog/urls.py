from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostEntries.as_view(), name='home'),
]