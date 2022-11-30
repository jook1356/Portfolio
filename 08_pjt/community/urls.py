from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/comments/<int:comment_pk>/create/', views.create_cocomment, name='create_cocomment'),
    path('<int:review_pk>/comments/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    path('<int:review_pk>/like/', views.like, name='like'),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comment_like, name="comment_like"),
    path('comments/delete/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
]
