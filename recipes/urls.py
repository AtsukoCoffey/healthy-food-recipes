from django.urls import path
from .views import AddRecipe, RecipeDetail

urlpatterns = [
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    # path('rate/<int:post_id>/<int:rating>/', views.rate),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
]