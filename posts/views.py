from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .models import Post, PostComment
from .forms import PostForm, PostCommentForm

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
    ``queryset``
        All the approved post article :model:`posts.Post`
    """
    template_name = "posts/posts.html"
    queryset = Post.objects.filter(approved=True)
    paginate_by = 6 
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        """
        1: For unapproved post author, show their unapproved post
        2: For owner search, send all the User model's name and pk and
        """
        context = super().get_context_data(**kwargs)
        # All the unapproved post's data
        context['unapproved'] = Post.objects.filter(approved=False)
        # All user's data
        context['all_users'] = User.objects.all()
        return context

    def get_queryset(self, **kwargs):
        """
        Search option modal's query
        Avoid/include words search - string
        owner_query - int (foreign key)
        """
        avoid_query = self.request.GET.get('q-avoid')
        include_query = self.request.GET.get('q-incl')
        owner_query = self.request.GET.get('q-owner')

        queryset = Post.objects.filter(approved=True)

        # Avoid and include words query
        if avoid_query:
            if include_query:
                queryset = queryset.exclude(
                    Q(title__icontains=avoid_query) |
                    Q(post_body__icontains=avoid_query)
                    ).filter(
                    Q(title__icontains=include_query) |
                    Q(post_body__icontains=include_query)
                    )
            else:
                queryset = queryset.exclude(
                    Q(title__icontains=avoid_query) |
                    Q(post_body__icontains=avoid_query)
                    )
        else:
            if include_query:
                queryset = queryset.filter(
                    Q(title__icontains=include_query) |
                    Q(post_body__icontains=include_query)
                    )

        # Owner search
        if owner_query:
            queryset = queryset.filter(Q(user=owner_query))
        return queryset


class PostDetail(DetailView):
    """
    Display a single post page :model:`posts.Post`
    **Context**
    ``post`` 
        An instance of :model:`posts.Post`
    ``form_class``
        form input for an instance :model:`posts.Post` 
    """
    template_name = "posts/post_detail.html"
    model = Post
    context_object_name = "post"
    form_class = PostCommentForm
    
    # queryset - approved post only
    def get_queryset(self, **kwargs):
        return Post.objects.filter(approved=True)

    # send the form_class to GET request 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    # POST request in CBV 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        slug = self.kwargs['slug']
        post = self.get_queryset().get(slug=slug)
        comments = post.comments.all()

        if form.is_valid():
            # <process form cleaned data>
            comment = form.save(commit=False)
            comment.post_commenter = request.user
            comment.post = post
            comment.save()
            # messages.add_message(
            #     request, messages.SUCCESS,
            #     'Comment submitted successfully'
            #  )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        return render(
            request, 
            "posts/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "form": form,
            }
            )


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