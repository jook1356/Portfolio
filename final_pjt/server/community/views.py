from .serializers import ReviewSerializer, CommentSerializer, LikeUsersSerializer, VisitSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from .models import Review, Comment



# Create your views here.
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by("-pk")
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def review_list_popular(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         reviews = reviews.extra(select={'popular'})
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
def review_list_visit(request):
    if request.method == 'GET':
        reviews = Review.objects.all().order_by('-visit__count')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def review_list_like(request):
    if request.method == 'GET':
        reviews = Review.objects.annotate(like_users_cnt=Count('like_users')).order_by('-like_users_cnt')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, id):
    review = Review.objects.get(pk=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            "result": f'{id}번 게시글이 삭제되었습니다. '
        }
        return Response(data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        movieId = request.data.get("movieId")
        if movieId != None:
            movie = Movie.objects.get(pk=movieId)
        if serializer.is_valid(raise_exception=True):
            if movieId == None:
                serializer.save(movie=None)
            else:
                serializer.save(movie=movie)
        return Response(serializer.data)
            



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_review(request):
    if request.method == 'POST':
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        movieId = request.data.get("movieId", -1)
        print(movieId)
        if movieId == -1:
            movie = -1
        else:
            movie = Movie.objects.get(pk=movieId)
        if serializer.is_valid(raise_exception=True):
            if movie == -1:
                serializer.save(user=user)
            else:
                serializer.save(user=user, movie=movie)
            return Response(serializer.data)


@api_view(['PUT'])
def review_count_visit(request, review_id):
    review = Review.objects.get(pk=review_id)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_comment(request):
    user = request.user
    reviewId = request.data["review"]
    review = Review.objects.get(pk=reviewId)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, review=review)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.order_by('pk').all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        data = {
            'result': f"{comment_pk}번 댓글을 삭제하였습니다."
        }
        return Response(data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST', 'GET'])
def review_like(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == "POST":
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            data = {
                'result': False
            }
        else: 
            review.like_users.add(request.user)
            data = {
                'result': True
            }
        return Response(data)
    elif request.method == 'GET':
        serializer = LikeUsersSerializer(review)
        return Response(serializer.data)


@api_view(['POST', 'PUT', 'GET'])
def visit(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        serializer = VisitSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        visit = review.visit_set.all()[0]
        serializer = VisitSerializer(visit, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        visit = review.visit_set.all()[0]
        serializer = VisitSerializer(visit)
        return Response(serializer.data)
