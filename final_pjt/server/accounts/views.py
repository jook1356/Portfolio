from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from community.serializers import ReviewSerializer, CommentSerializer, UserSerializer

# Create your views here.
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_comment(request, user_id):
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    comments = user.comment_set.order_by('-pk').all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_reviews(request, user_id):
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    reviews = user.review_set.order_by('-pk').all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_like_reviews(request, user_id):
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    reviews = user.like_reviews.order_by('-pk').all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


#-----------------------------------------------
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_additional_user_info(request):
    User = get_user_model()
    user = User.objects.get(pk=request.user.pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#-----------------------------------------------