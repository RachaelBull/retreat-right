from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import UsersPage
from .forms import UsersPageForm
from django.http import HttpResponseRedirect
from django.contrib import messages


class UserProfile(View):

    def get(self, request):
        user_profile_form = UsersPageForm
        userprofile = UsersPage.objects.all()
        return render(request,
            "userprofile/userprofile.html",
            {
            "userprofile": userprofile,
            'user_profile_form': user_profile_form
            })