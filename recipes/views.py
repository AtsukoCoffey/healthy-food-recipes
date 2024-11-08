# from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
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


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """Edit a recipe"""
    template_name ='recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_message = "Recipe was updated successfully"

    def test_func(self):
        return self.request.user == self.get_object().user

    # Return to the detail's page using 'get_success_url' and 'reverse'
    def get_success_url(self, **kwargs):
        if self.object.id != None:
            return reverse('recipe_detail', args=[self.object.id])
        else:
            return reverse('home')


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """Delete a recipe"""
    model = Recipe
    success_url = '/'
    success_message = "Recipe was deleted successfully"

    def test_func(self):
        return self.request.user == self.get_object().user