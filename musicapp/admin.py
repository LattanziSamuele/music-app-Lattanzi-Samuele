from django.contrib import admin
from .models import UserProfile, Song


admin.site.register(UserProfile)
admin.site.register(Song)
