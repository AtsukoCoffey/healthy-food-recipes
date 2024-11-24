from django.urls import path
from .views import AddPost
from . import views

urlpatterns = [
    path('add/', AddPost.as_view(), name='add_post'),
]