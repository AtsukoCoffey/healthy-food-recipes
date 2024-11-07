from django.urls import path
from .views import AddRecipe, RecipeDetail, EditRecipe

urlpatterns = [
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    # path('rate/<int:post_id>/<int:rating>/', views.rate),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe"),
]