from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:user_id>/', views.get_comment),
    path('reviews/<int:user_id>/', views.get_reviews),
    path('like_reviews/<int:user_id>/', views.get_like_reviews),
    path('get_additional_user_info/', views.get_additional_user_info),
]