from django.urls import path
from .views import AddRecipe, RecipeDetail, EditRecipe, DeleteRecipe
from . import views

urlpatterns = [
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    path("<slug:slug>/", views.RecipeDetail, name="recipe_detail"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>/",
        views.comment_edit, name='comment_edit'),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete, name='comment_delete'),
]
