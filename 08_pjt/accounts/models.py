from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    searched_movies = models.ManyToManyField(Movie, related_name='searched_users')
