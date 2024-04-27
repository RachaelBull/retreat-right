from django.shortcuts import render
from .models import userspage


def users_page(request):
    """
    Renders the Profile page
    """
    userprofile = userspage.objects.all()

    return render(
        request,
        "userprofile/userprofile.html",
        {"userprofile": userprofile},
    )