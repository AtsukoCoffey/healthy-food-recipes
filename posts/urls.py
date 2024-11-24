from django.urls import path
from .views import AddPost, Posts, PostDetail, EditPost, DeletePost
from . import views

urlpatterns = [
    path("add/", AddPost.as_view(), name='add_post'),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("edit/<slug:slug>/", EditPost.as_view(), name="edit_post"),
    path("delete/<slug:slug>/", DeletePost.as_view(), name="delete_post"),
    path("", Posts.as_view(), name="posts"),
]