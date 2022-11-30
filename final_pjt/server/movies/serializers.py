from rest_framework import serializers
from .models import Genre, Movie, Cast, GenreScore, MovieComment
from accounts.serializers import UserSerializer

class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class MovieListSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)
    dislike_users = UserSerializer(many=True, read_only=True)
    main_genre = GenreListSerializer(read_only=True)
    sub_genres = GenreListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'vote_average', 'vote_count')


class MovieLikeUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','like_users','dislike_users')


class MovieCastsListSetrializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    
    movie = MovieSerializer(read_only = True)

    class Meta:
        model = Cast
        fields = '__all__'

class MovieSortByGenreSerializer(serializers.ModelSerializer):

    # class MovieSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Movie
    #         fields = '__all__'
    
    movies = MovieListSerializer(many=True, read_only = True)
    
    class Meta:
        model = Genre
        fields = '__all__'
        
class GenreScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenreScore
        fields = '__all__'
        read_only = ('user', 'genre', )


class CommentSerializer(serializers.ModelSerializer):
    class MovieSerializerForComment(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')
    user = UserSerializer(read_only=True)
    movie = MovieSerializerForComment(read_only=True)
    created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M", read_only=True)


    class Meta:
        model = MovieComment
        fields = '__all__'