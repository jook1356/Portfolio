from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import Genre, Movie, Cast
from .models import Genre, Movie, Cast
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieListSerializer, GenreListSerializer, MovieCastsListSetrializer, MovieLikeUsersSerializer, MovieSortByGenreSerializer, GenreScoreSerializer, MovieUpdateSerializer, CommentSerializer
from .models import Genre, Movie, Cast, MovieRecommend, GenreScore, MovieComment
from accounts.models import User
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

from django.db.models import Count
import pandas
from django.db.models import Q

# Create your views here.

@api_view(['GET'])
def get_genre_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def get_all_movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)





@api_view(['GET'])
def get_top_rated_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-general_vote_weight')[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

#------------------------------------------------------------------------
@api_view(['GET'])
def get_movie_casts(request, movie_id):

    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_id)
        casts = movie.casts.all()
        serializer = MovieCastsListSetrializer(casts, many=True)
        return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def like_movie(request, movie_id):
    
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        
        serializer = MovieLikeUsersSerializer(movie)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def dislike_movie(request, movie_id):
    
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        if movie.dislike_users.filter(pk=request.user.pk).exists():
            movie.dislike_users.remove(request.user)
        else:
            movie.dislike_users.add(request.user)
        
        serializer = MovieLikeUsersSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def get_movie_likes(request, movie_id):
    
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_id)
        serializer = MovieLikeUsersSerializer(movie)
        return Response(serializer.data)
        


@api_view(['GET'])
def get_movies_by_genre(request, genre):
    if request.method == 'GET':
        if genre == 'all':
            genres = get_list_or_404(Genre)
            serializer = MovieSortByGenreSerializer(genres, many=True)
        else:
            genres = Genre.objects.filter(id=genre)
            serializer = MovieSortByGenreSerializer(genres, many=True)
        
        return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def store_selected_movies(request, user_id):
    if request.method == 'POST':
        movies = request.data['selectedMovies']
        for movie in movies:
            movie = Movie.objects.get(pk=movie['id'])
            movie.selected_users.add(user_id)
        
        user = User.objects.get(pk=user_id)
        user.new_user = False
        user.save()
        return Response(request.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def store_viewed_movies(request, user_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=request.data['movieId'])
        movie.viewed_users.add(user_id) 
        return Response(request.data)


@api_view(['GET'])
def recommend_most_viewed(request):
    if request.method == 'GET':
        movies = Movie.objects.all().annotate(count=Count('viewed_users')).order_by('-count')[:50]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_popular_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all().annotate(count=Count('like_users')).order_by('-count')[:100]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

#         queryset1 = Model.objects.all()
# count = queryset1.aggregate(count=Count('id'))

@api_view(['GET'])
def recommend_general(request):
    movies = Movie.objects.all()
    data = pandas.DataFrame(data=Movie.objects.all().values('id', 'vote_average', 'vote_count'))
    
    vote_standard = data['vote_count'].quantile(0.95)
    movies_vote_average = sum(data['vote_average']) / len(data['vote_average'])

    for i in range(len(data['id'])):
        movie = Movie.objects.get(pk=data['id'][i])
        if data['vote_count'][i] >= vote_standard:
            movie_vote_count = data['vote_count'][i]
            movie_rated_average = data['vote_average'][i]
            movies_vote_weight = (movie_vote_count/(movie_vote_count + vote_standard) * movie_rated_average) + (vote_standard/(vote_standard + movie_vote_count) * movies_vote_average)
            movie.general_vote_weight = movies_vote_weight
            movie.save()
        else:
            movie.general_vote_weight = 0
            movie.save()

    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def recommend_related(request):
    if request.method == 'POST':
        # 1. 해당 유저가 좋아요 한 영화들에 좋아요를 누른 다른 유저들의 정보를 가져온다.
        movies = Movie.objects.all()
        related_users = set()
        for movie in movies:
            if movie.like_users.filter(pk=request.user.pk).exists():
                for user in movie.like_users.values('id'):
                    related_users.add(user['id'])
        users = get_user_model().objects.all()
        
        # 2. 가져온 유저들이 좋아요를 누른 영화들의 정보를 가져온다.
        # 이때, 영화 중복 체크를 하고 중복이 나온 영화들은 가중치에 보너스 점수로 치환된다.
        duplicate_check = []
        related_movies = []
        for user in users[1:]:
            
            for movie in user.like_movies.values():
                if movie['id'] not in duplicate_check:
                    # related_movies.append(movie)
                    related_movies.append(movie['id'])
                    duplicate_check.append(movie['id'])
                else:
                    duplicate_check.append(movie['id'])

        # 3. DB에서 기존에 남아있던 데이터를 모두 삭제한다.
        remained_movies = MovieRecommend.objects.filter(Q(user=request.user) & ~Q(related_vote_weight=None))
        remained_movies.delete()

        # 4. 가중치 계산을 위한 통계를 구한다.
        user_movies = Movie.objects.filter(id__in=related_movies)
        data = pandas.DataFrame(data=user_movies.values('id', 'vote_average', 'vote_count'))
        vote_standard = data['vote_count'].quantile(0.95)
        movies_vote_average = sum(data['vote_average']) / len(data['vote_average'])

        # 5. 가중치의 공식은 아래와 같다. 일반적인 가중치에 보너스 점수를 추가한다.
        for i in range(len(data['id'])):
            movie_vote_count = data['vote_count'][i]
            movie_rated_average = data['vote_average'][i]
            duplicate_bonus = duplicate_check.count(data['id'][i]) * 0.01
            movie_vote_weight = (movie_vote_count/(movie_vote_count + vote_standard) * movie_rated_average) + (vote_standard/(vote_standard + movie_vote_count) * movies_vote_average) + duplicate_bonus
            MovieRecommend.objects.create(movie=user_movies[i], user=request.user, related_vote_weight=movie_vote_weight)


        # 6. 가중치를 기준으로 해당 유저에 해당하는 영화들을 가져와서 가공한다.
        recommend = MovieRecommend.objects.filter(user=request.user).order_by('-related_vote_weight')
        extracted_movies = []
        for i in range(len(recommend)):
            extracted_movies.append(recommend[i].movie)
        
        serializer = MovieListSerializer(extracted_movies, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def calculate_score(request):
    if request.method == 'POST':
        
        # 1. 점수 계산이 필요한 장르들과 점수를 받는다. (좋아요, 싫어요, 영화 상세 페이지 조회, 회원가입 영화 선택 시)
        # 이때 점수는 메인 장르의 점수 상승/하락 폭과 서브 장르의 점수 상승/하락 폭이 다르다.
        genre_score_set = request.data['genreScoreSet']
        main_genres = genre_score_set['main_genres']
        sub_genres = genre_score_set['sub_genres']

        # 2. 메인 장르와 서브 장르들을 나눠서 점수 계산을 하여 딕셔너리에 저장한다.
        calculated = {}
        for i in range(len(main_genres)):
            if calculated.get(main_genres[i]['id']):
                calculated[main_genres[i]['id']] += genre_score_set['main_genre_score']
            else:
                calculated[main_genres[i]['id']] = genre_score_set['main_genre_score']
        
        for i in range(len(sub_genres)):
            for j in range(len(sub_genres[i])):
                if calculated.get(sub_genres[i][j]['id']):
                    calculated[sub_genres[i][j]['id']] += genre_score_set['sub_genre_score']
                else:
                    calculated[sub_genres[i][j]['id']] = genre_score_set['sub_genre_score']
        
        # 3. 계산한 장르의 점수를 DB에 반영한다.
        for genre, score in calculated.items():
            genre_model = Genre.objects.filter(id=genre)
            genre_score_model = GenreScore.objects.filter(Q(user=request.user) & Q(genre=genre_model[0]))
            if genre_score_model.exists():
                sum_score = genre_score_model[0].score + score
                genre_score_model.update(score=sum_score)
            else:
                GenreScore.objects.create(genre=genre_model[0], user=request.user, score=score)
        
        genre_scores = GenreScore.objects.filter(user=request.user)
        serializer = GenreScoreSerializer(genre_scores, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def recommend_score(request):
    if request.method == 'POST':

        # 1. 해당 회원의 유효한 점수를 가진 장르들을 불러온 후, 영화를 불러온다.
        # 이때, 장르들의 점수는 가중치에 1/100의 비율의 보너스 점수로 치환된다.
        scores = GenreScore.objects.filter(user=request.user).order_by('-score').values('genre', 'score')[:3]
        movies = []
        bonus_score = {}
        for i in range(len(scores)):
            queryset = Movie.objects.filter(main_genre=scores[i]['genre'])
            movies.append(queryset)
            bonus_score[scores[i]['genre']] = scores[i]['score'] / 100

        # 2. 불러온 장르들에 해당하는 영화들을 하나의 쿼리셋으로 합친다. (union)
        total_movies = movies[0]
        for i in range(1, len(movies)):
            total_movies = total_movies.union(movies[i])

        # 3. DB에서 기존에 남아있던 데이터를 모두 삭제한다.
        remained_movies = MovieRecommend.objects.filter(Q(user=request.user) & ~Q(score_vote_weight=None))
        remained_movies.delete()

        # 4. 가중치 계산을 위한 통계를 구한다.
        data = pandas.DataFrame(data=total_movies.values('id', 'vote_average', 'vote_count', 'main_genre'))
        vote_standard = data['vote_count'].quantile(0.95)
        movies_vote_average = sum(data['vote_average']) / len(data['vote_average'])
        
        # 5. 가중치의 공식은 아래와 같다. 일반적인 가중치에 보너스 점수를 추가한다.
        for i in range(len(data['id'])):
            movie_vote_count = data['vote_count'][i]
            movie_rated_average = data['vote_average'][i]
            movie_bonus_score = bonus_score[data['main_genre'][i]]
            movie_vote_weight = (movie_vote_count/(movie_vote_count + vote_standard) * movie_rated_average) + (vote_standard/(vote_standard + movie_vote_count) * movies_vote_average) + movie_bonus_score
            MovieRecommend.objects.create(movie=total_movies[i], user=request.user, score_vote_weight=movie_vote_weight)

        # 6. 가중치를 기준으로 해당 유저에 해당하는 영화들을 가져와서 가공한다.
        recommend = MovieRecommend.objects.filter(user=request.user).order_by('-score_vote_weight')
        extracted_movies = []
        for i in range(len(recommend)):
            extracted_movies.append(recommend[i].movie)
        
        serializer = MovieListSerializer(extracted_movies, many=True)
        return Response(serializer.data)

    



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_comment(request):
    data = request.data
    user = request.user
    movieId = request.data['movie']
    movie = Movie.objects.get(pk=movieId)
    print(data)
    is_valid = MovieComment.objects.filter(Q(movie=movie) & Q(user=user) & ~Q(vote=None))
    if data['vote'] != 0:
        if is_valid.exists():
            # for comment in is_valid:
                # movie_vote_total = ((movie.vote_count * movie.vote_average) - comment.vote) / (movie.vote_count - 1)
            movie_vote_total = ((movie.vote_count * movie.vote_average) - is_valid[0].vote + data['vote']) / movie.vote_count
            movie.vote_average = movie_vote_total
            movie.save()
            is_valid.update(vote=None)
        else:
            movie_vote_total = ((movie.vote_count * movie.vote_average) + data['vote']) / (movie.vote_count + 1)
            count = movie.vote_count + 1
            movie.vote_average = movie_vote_total
            movie.vote_count = count
            movie.save()

    serializer = CommentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        
    comments = movie.moviecomment_set.order_by('-pk').all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def comment_list(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.moviecomment_set.order_by('-pk').all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = MovieComment.objects.get(pk=comment_pk)
    
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=comment.movie.pk)
        movie_vote_total = ((movie.vote_count * movie.vote_average) - comment.vote) / (movie.vote_count - 1)
        count = movie.vote_count - 1
        movie.vote_average = movie_vote_total
        movie.vote_count = count
        movie.save()
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
@api_view(['POST'])
def off_new_user(request):
    if request.method == 'POST':
        user = get_user_model().objects.get(pk=request.user.pk)
        user.new_user = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


    
#------------------------------------------------------------------------


@api_view(['GET'])
def get_search_movies(request):
    searchWord = request.GET['searchWord']
    searchMovieList = Movie.objects.filter(title__contains=searchWord)
    serializer = MovieListSerializer(searchMovieList, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def update_movie_vote(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        serializer = MovieUpdateSerializer(movie, request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = MovieUpdateSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)
