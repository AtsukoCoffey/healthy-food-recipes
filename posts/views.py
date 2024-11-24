from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    ``queryset``
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