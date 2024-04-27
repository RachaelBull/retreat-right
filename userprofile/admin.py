from django.contrib import admin
from .models import userspage
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(userspage)






#@admin.register(userspage)
#class ProfilesAdmin(SummernoteModelAdmin):

  #  summernote_fields = ('bio',)