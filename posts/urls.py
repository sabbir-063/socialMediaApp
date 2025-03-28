from django.urls import path
from .views import create_post, like_post, update_post, delete_post, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_post, name='create_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('update/<int:post_id>/', update_post, name='update_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
