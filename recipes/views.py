from django.shortcuts import render, get_object_or_404
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


# If user is authenticated and rated before display the rate, or 0 star
# Took this out from Detail view to call before and after processing POST
def get_user_rating(user, recipe):
    if user.is_authenticated:
        rating = Rating.objects.filter(recipe=recipe, user=user).first()
        return rating.rating if rating else 0
    else: 
        return 0


def RecipeDetail(request: HttpRequest, slug) -> HttpResponse:
    """
    Display a single recipe page :model:`recipes.Recipe`
    **Context**
    ``recipe`` An instance of :model:`recipes.Recipe`
    ``rating`` An instance of :model:`recipes.Rating`
    ``comments`` All comments related to the recipe.
    """
    recipe = get_object_or_404(Recipe.objects.all(), slug=slug)

    # Call user rating function : ->move to outside of this function view
    user_rating = get_user_rating(request.user, recipe)

    # Update or create the rating for this unique user and recipe
    if request.method == "POST":
        rate_value = request.POST.get("rate")
        if rate_value == None:
            rate_value = 0
        Rating.objects.update_or_create(
            recipe=recipe,
            user=request.user,
            defaults={"rating": rate_value}  # rating is the field of rating model
        )
        # Call user rating function again
        user_rating = get_user_rating(request.user, recipe)
        print(user_rating)

    return render(
        request, 
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "user_rating": user_rating,
        }
    )


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
            return reverse('recipe_detail', args=[self.object.slug])
        else:
            return reverse('home')


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """Delete a recipe"""
    model = Recipe
    success_url = '/'
    success_message = "Recipe was deleted successfully"

    def test_func(self):
        return self.request.user == self.get_object().user