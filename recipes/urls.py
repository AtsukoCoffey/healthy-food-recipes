from django.urls import path
from .views import AddRecipe, RecipeDetail, EditRecipe, DeleteRecipe
from . import views

urlpatterns = [
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    path('rate/<int:recipe_id>/<int:rating>/', views.rate),
    path("<slug:slug>/", views.RecipeDetail, name="recipe_detail"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
]