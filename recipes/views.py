# from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Recipe
from .forms import RecipeForm


class AddRecipe(CreateView):
    """Add recipe view"""

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


