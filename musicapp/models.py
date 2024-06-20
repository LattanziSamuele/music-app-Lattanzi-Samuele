from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=5)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=100, choices=(
            ('Rock', 'Rock'),
            ('Pop', 'Pop'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Jazz', 'Jazz'),
            ('Classical', 'Classical'),
            ('Electronic', 'Electronic'),
            ('Country', 'Country'),
            ('Kpop', 'Kpop'),
    ), blank=True)

    def __str__(self):
        return self.user.username


