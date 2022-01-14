from django.contrib import admin
from django.contrib.auth.models import User

from app.profile.models import ProfileFirst, Profile


class ProfileFirstAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email"]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "first_name", "last_name", "age"]

admin.site.register(ProfileFirst, ProfileFirstAdmin)
admin.site.register(Profile, ProfileAdmin)