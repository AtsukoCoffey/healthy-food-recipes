from django.urls import path
from .views import AddPost, Posts
from . import views

urlpatterns = [
    path('add/', AddPost.as_view(), name='add_post'),
     path("", Posts.as_view(), name="posts"),
]