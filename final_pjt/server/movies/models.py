from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_genres")


class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    logo_path = models.CharField(max_length=500, null=True)
    # genres = models.ManyToManyField(Genre, related_name="movies")
    main_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies")
    sub_genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dislike_movies", blank=True)
    selected_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="selected_movies", blank=True)
    viewed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="viewed_movies", blank=True)
    general_vote_weight = models.FloatField(null = True)


class GenreScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="user_score")
    score = models.FloatField()


class MovieRecommend(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommend_movie')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    related_vote_weight = models.FloatField(null=True)
    score_vote_weight = models.FloatField(null=True)




class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    known_for_department = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=500, null=True)
    character = models.CharField(max_length=100)
    credit_id = models.CharField(max_length=100)


class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    vote = models.FloatField(null=True)


