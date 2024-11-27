from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import BadRequest
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
    paginate_by = 9
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
        queryset = Post.objects.filter(approved=True)
        avoid_query = self.request.GET.get('q-avoid')
        include_query = self.request.GET.get('q-incl')
        owner_query = self.request.GET.get('q-owner')

        # From queryset flter Avoid query 
        if avoid_query:
            queryset = queryset.exclude(
                Q(title__icontains=avoid_query) |
                Q(post_body__icontains=avoid_query)
            )
        # filter include query
        if include_query:
            queryset = queryset.filter(
                Q(title__icontains=include_query) |
                Q(post_body__icontains=include_query)
            )
        # Owner search
        if owner_query:
            try:
                owner_id = int(owner_query)
                queryset = queryset.filter(user_id=owner_id)
            except ValueError:
                raise BadRequest("Invalid owner! Try again!")
        return queryset


class PostDetail(SuccessMessageMixin, DetailView):
    """
    Display a single post page :model:`posts.Post`
    **Context**
    ``post``
        Queryset object An instance of :model:`posts.Post`
    ``form``
        form_class input for an instance :model:`posts.PostComment`
    ``comments``
        All the relavent comments that are filtered by Post's conditions
    """
    template_name = "posts/post_detail.html"
    # model = Post
    # context_object_name = "post"
    # queryset = Post.objects.all()
    form_class = PostCommentForm
    success_message = "Comment for this post was created successfully"

    # queryset - approved post only
    def get_queryset(self, **kwargs):
        return Post.objects.all()

    # send the form_class to GET request
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()  
        context['comments'] = self.get_queryset(
            # 'slug=self.kwargs['slug']' means similar to 'slug=slug'
            ).get(slug=self.kwargs['slug']).comments.all()
        return context

    # POST request in CBV
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        slug = self.kwargs['slug']

        try:  # In case of Non try and catch
            post = self.get_queryset().get(slug=slug)
        except Post.DoesNotExist:
            raise Http404("There is no approved post yet. Post not found.")        
        # The model for the form is PostComment
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.post = post
            comment.save()
            # Add success message manually
            messages.success(request, self.success_message)
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        # comments assign again 
        comments = post.comments.all()
        return render(
            request,
            self.template_name,
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
    template_name = 'posts/edit_post.html'
    model = Post
    form_class = PostForm
    success_url = '/posts/'

    # security
    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePost(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
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


@login_required
def comment_edit(request, slug, comment_id):
    """
    Display an individual post's comment for edit.
    **Context**
    ``post``
        An instance of :model:`posts.Post`.
    ``comment``
        A single comment related to the post.
    ``form``
        An isntance of :form:`posts.PostCommentForm`.
    """
    if request.method == "POST":
        posts = Post.objects.all()
        post = get_object_or_404(posts, slug=slug)
        comment = get_object_or_404(PostComment, pk=comment_id)
        form = PostCommentForm(data=request.POST, instance=comment)
        # form validation and "user = commenter" check 
        if form.is_valid() and comment.commenter == request.user:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.
    **Context**
    ``post``
        An instance of :model:`posts.Post`.
    ``comment``
        A single comment related to the post.
    """
    posts = Post.objects.all()
    post = get_object_or_404(posts, slug=slug)
    comment = get_object_or_404(PostComment, pk=comment_id)

    #  "user = commenter" check 
    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))