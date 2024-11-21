from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Recipe, Rating, RecipeComment
from .forms import RecipeForm, RecipeCommentForm


class AddRecipe(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add - create new - recipe view
    **Template:**
    :template:`recipes/add_recipe.html`
     **Context**
    ``form_class``
        form input for an instance :model:`recipes.Recipe`
    """
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


# If user is authenticated and rated before display the rating, or 0 star
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
    # get comment data using the related_name 
    comments = recipe.comments.all().order_by("-posted_date")

    if request.method == "POST":
        # For Comment posting
        comment_form = RecipeCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted successfully'
             )

        # Update or create the rating for this unique user and recipe
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
        # Redirect to avoid form resubmission
        return redirect('recipe_detail', slug=slug)
    
    comment_form = RecipeCommentForm()
    return render(
        request, 
        "recipes/recipe_detail.html",
        {
            'recipe': recipe,
            'user_rating': user_rating,
            'comments': comments,
            "comment_form": comment_form,
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


def comment_edit(request, slug, comment_id):
    """
    Display an individual recipe's comment for edit.
    **Context**
    ``recipe``
        An instance of :model:`recipes.Recipe`.
    ``comment``
        A single comment related to the recipe.
    ``comment_form``
        An isntance of :form:`recipes.RecipeCommentForm`.
    """
    if request.method == "POST":
        recipes = Recipe.objects.all()
        recipe = get_object_or_404(recipes, slug=slug)
        comment = get_object_or_404(RecipeComment, pk=comment_id)
        comment_form = RecipeCommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.
    **Context**
    ``recipe``
        An instance of :model:`recipes.Recipe`.
    ``comment``
        A single comment related to the recipe.
    """
    recipes = Recipe.objects.all()
    recipe = get_object_or_404(recipes, slug=slug)
    comment = get_object_or_404(RecipeComment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))