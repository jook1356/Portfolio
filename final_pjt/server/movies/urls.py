from django.urls import path, include
from . import views

urlpatterns = [
    path('get_genre_list/', views.get_genre_list),
    path('get_all_movies/', views.get_all_movies),
    path('get_popular_movies/', views.get_popular_movies),
    path('get_top_rated_movies/', views.get_top_rated_movies),
    #------------------------------------------------------------
    path('get_movie_casts/<int:movie_id>/', views.get_movie_casts),
    path('like_movie/<int:movie_id>/', views.like_movie),
    path('dislike_movie/<int:movie_id>/', views.dislike_movie),
    path('get_movie_likes/<int:movie_id>/', views.get_movie_likes),
    path('get_movies_by_genre/<str:genre>/', views.get_movies_by_genre),
    path('recommend_most_viewed/', views.recommend_most_viewed),
    path('recommend_general/', views.recommend_general),
    path('recommend_related/', views.recommend_related),
    path('recommend_score/', views.recommend_score),
    path('calculate_score/', views.calculate_score),
    path('store_selected_movies/<int:user_id>/', views.store_selected_movies),
    path('store_viewed_movies/<int:user_id>/', views.store_viewed_movies),
    path('create_comment/', views.create_comment),
    path('comment_list/<int:movie_pk>/', views.comment_list),
    path('comment_detail/<int:comment_pk>/', views.comment_detail),
    path('off_new_user/', views.off_new_user),

    #------------------------------------------------------------
    path('get_search_movies/', views.get_search_movies),
    path('update_movie_vote/<int:movie_id>/', views.update_movie_vote),
    path('movie_detail/<int:movie_id>/', views.movie_detail),

]
