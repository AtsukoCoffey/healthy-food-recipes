from django.urls import path
from .views import AddPost, Posts, PostDetail
from . import views

urlpatterns = [
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path('add/', AddPost.as_view(), name='add_post'),
    path("", Posts.as_view(), name="posts"),
]