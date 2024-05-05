from .models import UsersPage
from django import forms

class UsersPageForm(forms.ModelForm):
    class Meta:
        model = UsersPage
        fields = ('name', 'email', 'bio')

        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'bio': 'About You'
        }