from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
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
    success_url = "/"
    success_message = "Post was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )


class Posts(ListView):
    """
    All the Posts list view - posts top page
    """
    template_name = "posts/posts.html"
    model = Post
    context_object_name = "posts"

