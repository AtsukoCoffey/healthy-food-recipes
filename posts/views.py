from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .models import Post
from .forms import PostForm

class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add - create new - post
    **Template:**
    :template:`posts/add_post.html`
    **Context**
    ``form_class``
        form input for an instance :model:`posts.Post`
    ``title``
        for message - post's title
    """
    template_name = "posts/add_post.html"
    model = Post
    form_class = PostForm
    success_message = "Post was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

    # Return to the detail's page using 'get_success_url' and 'reverse'
    def get_success_url(self, **kwargs):
        if self.object.id != None:
            return reverse('post_detail', args=[self.object.slug])
        else:
            return reverse('posts')


class Posts(ListView):
    """
    Add - the Posts list view - posts top page
    **Template:**
    :template:`posts/posts.html`
    **Context**
    ``posts``
        All the post article :model:`posts.Post`
    """
    template_name = "posts/posts.html"
    model = Post
    paginate_by = 8
    context_object_name = "posts"


class PostDetail(DetailView):
    """
    Display a single post page :model:`posts.Post`
    **Context**
    ``post`` An instance of :model:`posts.Post`
    """
    template_name = "posts/post_detail.html"
    model = Post
    context_object_name = "post"


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a single post page :model:`posts.Post`
    **Context**
    ``form_class``
        form input for an instance :model:`posts.Post`
    ``post`` An instance of :model:`posts.Post`
    """
    template_name ='posts/edit_post.html'
    model = Post
    form_class = PostForm
    success_url = '/posts/'

    # security
    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    Delete a single post page :model:`posts.Post`
    **Context**
    ``object`` An instance of :model:`posts.Post`
    """
    model = Post
    success_url = '/posts/'
    success_message = "Post was deleted successfully"

    # security
    def test_func(self):
        return self.request.user == self.get_object().user