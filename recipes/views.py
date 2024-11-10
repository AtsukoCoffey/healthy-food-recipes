from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .models import Recipe, Rating
from .forms import RecipeForm


class AddRecipe(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add - create new - recipe view"""
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/"
    success_message = "Recipe was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )


class RecipeDetail(DetailView):
    """
    Display a single recipe page :model:`recipes.Recipe`
    **Context**
    ``recipe`` An instance of :model:`recipes.Recipe`
    ``rating`` An instance of :model:`recipes.Rating`
    ``comments`` All comments related to the recipe.
    """
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


def update_rating(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all()
    for recipe in recipes:
        rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
        recipe.user_rating = rating.rating if rating else 0
    return render(request, "recipes/recipe_detail.html", {"recipes": recipes})


def rate(request: HttpRequest, recipe_id: int, rating: int) -> HttpResponse:
    recipe = Recipe.objects.get(id=recipe_id)
    Rating.objects.filter(recipe=recipe, user=request.user).delete()
    recipe.rating_set.create(user=request.user, rating=rating)
    return update_rating(request)


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