from rest_framework import serializers
from .models import Review, Comment, Visit
from movies.models import Movie
from accounts.serializers import UserSerializer




class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        read_only_fields = ('review', )


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('id', 'title', )
    class VisitSerializer(serializers.ModelSerializer):
        class Meta:
            model = Visit
            fields = ('count', )
    visit_set = VisitSerializer(many=True, read_only=True)
    movie = MovieSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class RevieWSerializerForComment(serializers.ModelSerializer):
        comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
        class Meta:
            model = Review
            fields = ('id', 'title', 'comment_count', )
    user = UserSerializer(read_only=True)
    review = RevieWSerializerForComment(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class LikeUsersSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ('like_users', )


