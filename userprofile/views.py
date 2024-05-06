from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import UsersPage, User
from .forms import UsersPageForm
from django.http import HttpResponseRedirect
from django.contrib import messages


class UserProfile(View):

    def get(self, request):
       if request.user.is_authenticated:
            # if the users profile already exists
            if UsersPage.objects.filter(user=request.user).exists():
                user_profile_instance = UsersPage.objects.get(user=request.user)
                user_profile_form = UsersPageForm(instance=user_profile_instance)
            else:
                user_profile_form = UsersPageForm()

            return render(request, "userprofile/userprofile.html",
            {
                'user_profile_form': user_profile_form
            })

    def post(self,request):
        user_profile_instance = None
        if UsersPage.objects.filter(user=request.user).exists():
            user_profile_instance = UsersPage.objects.get(user=request.user)

        user_profile_form = UsersPageForm(request.POST, instance=user_profile_instance)
        if user_profile_form.is_valid():
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            if user_profile_instance:
                messages.success(request, "Your profile has been updated.")
            else:
                messages.success(request, "Your profile has been created.")

            return redirect('home')

        return render(request, "userprofile/userprofile.html", {'user_profile_form: user_profile_form'})               