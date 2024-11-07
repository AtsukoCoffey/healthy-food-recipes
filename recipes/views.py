# from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Recipe
from .forms import RecipeForm


class AddRecipe(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add - create new - recipe view"""

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/"
    success_message = "Recipe was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class RecipeDetail(DetailView):
    """View a single recipe page"""

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


