from django.urls import path
from .views import AddRecipe

urlpatterns = [
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    # path('rate/<int:post_id>/<int:rating>/', views.rate),
]