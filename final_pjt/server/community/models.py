from django.db import models
from django.conf import settings

from movies.models import Movie

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    vote = models.FloatField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews", blank=True)


class Visit(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
