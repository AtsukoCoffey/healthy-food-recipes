from django.urls import path
from .views import AddPost, Posts, PostDetail
from . import views

urlpatterns = [
    path("add/", AddPost.as_view(), name='add_post'),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("", Posts.as_view(), name="posts"),
]