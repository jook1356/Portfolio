from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:id>/', views.review_detail),
    path('review/list/', views.review_list),
    path('review/list/visit/', views.review_list_visit),
    path('review/list/like/', views.review_list_like),
    path('review/count_visit/<int:review_id>/', views.review_count_visit),
    path('review/like/<int:review_id>/', views.review_like),
    path('review/create/', views.create_review),
    path('comment/visit/<int:review_pk>/', views.visit),
    path('comment/create/', views.create_comment),
    path('comment/list/<int:review_pk>/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
]