# python manage.py loaddata genre_data.json movie_data.json cast_data.json
# load순서 주의하기(순서 틀리면 로드 안됨)

import requests
import json

TMDB_API_KEY = '59f37ea0fe45bc22b119831a477faf25'

def get_movie_datas():
    movie_total_data = []
    cast_total_data = []

    idx = 1

    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            
            if movie.get('release_date', '') and movie.get('backdrop_path', '') and len(movie['genre_ids']) > 0:
                # movie의 출연진 가지고 오기
                casts_list = []
                cast_request_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                casts = requests.get(cast_request_url).json()
                for cast in casts["cast"]:
                    cast_fields = {  # cast모델 fixtures만들어주기
                        'movie_id': movie["id"],
                        'name': cast["name"],
                        'order': cast["order"],
                        'known_for_department': cast["known_for_department"],
                        'original_name': cast["original_name"],
                        'profile_path': cast["profile_path"],
                        'character': cast["character"],
                        'credit_id': cast["credit_id"],

                    }

                    cast_data = {
                        "pk": idx,
                        "model": "movies.cast",
                        "fields": cast_fields
                    }
                    cast_total_data.append(cast_data)
                    idx += 1
                image = f"https://api.themoviedb.org/3/movie/{movie['id']}/images?api_key={TMDB_API_KEY}"
                logo = requests.get(image).json()['logos']

                if logo != []:
                    logo_path = logo[0]['file_path']
                else:
                    logo_path = None

                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'vote_average': movie['vote_average'] / 2,
                    'vote_count': movie['vote_count'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path': movie['backdrop_path'],
                    'main_genre': movie['genre_ids'][0],
                    'sub_genres': movie['genre_ids'][1:],
                    'logo_path': logo_path,
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                movie_total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(movie_total_data, w, indent=4, ensure_ascii=False)

    with open("movies/fixtures/cast_data.json", "w", encoding="utf-8") as w:
        json.dump(cast_total_data, w, indent=4, ensure_ascii=False)


def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)



get_movie_datas()
get_genre_data()