from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from .models import Movie, Genre



# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()

    if request.user.is_authenticated:
        user = request.user
        user.searched_movies.add(movie)


    context = {
        'movie': movie,
        'genres': genres,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:


        user = request.user
        if user.searched_movies.all().exists():
            movies = user.searched_movies.all()
            genres = {}
            for movie in movies:
                for genre in movie.genres.all():
                    if genres.get(genre.name):
                        genres[genre.name] += 1
                    else:
                        genres[genre.name] = 1

            genres = sorted(genres.items(), key = lambda x : x[1], reverse=True)
            # fav_genre = genres[0][0]

            movies = Movie.objects.order_by('-vote_average')
            recommended_movies = {}
            for fav_genre in genres:
                for movie in movies:
                    for genre in movie.genres.all():
                        if genre.name == fav_genre[0]:
                            if recommended_movies.get(genre.name):
                                recommended_movies[genre.name].append(movie)
                            else:
                                recommended_movies[genre.name] = [movie]
                            break
            

            output_movies = set()
            for key in recommended_movies.keys():
                idx = 0
                for movie in recommended_movies[key]:
                    if idx < 3:
                        output_movies.add(movie)
                        idx += 1

            genres_str = []
            for i in genres:
                genres_str.append(i[0])
            genres_str = ', '.join(genres_str[:5])
            is_exist = True

            output_movies = list(output_movies)
        else:
            output_movies = Movie.objects.order_by('-vote_average')[:10]
            genres_str = '영화를 조회한 이력을 찾을 수 없으므로 평점 순으로 표시합니다.'
            is_exist = False

        context = {
            'movies': output_movies,
            'genres': genres_str,
            'is_exist': is_exist,
        }

        return render(request, 'movies/recommended.html', context)



@require_POST
def init_recommended(request):
    if request.user.is_authenticated:
        
        request.user.searched_movies.all().delete()
        genres_str = '페이지를 새로고침 하세요.'
        is_exist = False
        context = {
            'genres': genres_str,
            'is_exist': is_exist,
        }
        return JsonResponse(context)
    return redirect('accounts:login')