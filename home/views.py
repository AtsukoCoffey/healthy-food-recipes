from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.models import User
from recipes.models import Recipe
from posts.models import Post


class Index(ListView):
    """
    Display the list of the recipes
    **Template:**
    :template:`home/index.html`
    **Context**
    ``queryset``
        All recipes :model:`recipes.Recipe` and queried recipes -get_queryset
    ``context['query_string']``
        Keep the GET parameters to context when using pagination
    ``context['all_users']``
        All users data for option search display
    """
    template_name = 'home/index.html'
    context_object_name = 'recipes'
    paginate_by = 9
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        """
        1: For pagination issue, keep the GET request(filters) to the context
        2: For owner search, send all the User model's name and pk and
        """
        context = super().get_context_data(**kwargs)
        # Add GET parameters to context
        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')
        context['query_string'] = query_params.urlencode()
        # All user's data
        context['all_users'] = User.objects.all()
        # Post articles - Slice 3 objects from newest order
        context['posts3'] = Post.objects.filter(
            approved=True).order_by('-posted_date')[:3]
        return context

    def get_queryset(self, **kwargs):
        """
        Search option modal's query
        8 checkboxes - on or None
        owner_query - int (foreign key)
        others are - string
        """
        avoid_query = self.request.GET.get('q-avoid')
        include_query = self.request.GET.get('q-incl')
        owner_query = self.request.GET.get('q-owner')
        free_query = self.request.GET.get('q-free')

        queryset = Recipe.objects.all()

        # 8 checkboxs all the combination query
        # Save the "on" checkbox field in `filters` dictionary
        filters = {}
        for field in [
                'lowsugar',
                'glutenfree',
                'dairyfree',
                'vegan',
                'vegitarian',
                'highfiber',
                'highprotein',
                'nutfree']:
            if self.request.GET.get(field):
                filters[field] = True
        # The filter dictionary goes in the kwargs as like `lowsugar=True`
        if filters:
            queryset = queryset.filter(**filters)

        # Avoid and include Ingredients query
        if avoid_query:
            if include_query:
                queryset = queryset.exclude(
                    ingredients__icontains=avoid_query).filter(
                    Q(ingredients__icontains=include_query))
            else:
                queryset = queryset.exclude(
                    ingredients__icontains=avoid_query)
        else:
            if include_query:
                queryset = queryset.filter(
                    Q(ingredients__icontains=include_query))

        # Free search in Title, Description, Instruction
        if free_query:
            queryset = queryset.filter(
                Q(title__icontains=free_query) |
                Q(description__icontains=free_query) |
                Q(instructions__icontains=free_query)
            )

        # Owner search
        if owner_query:
            queryset = queryset.filter(Q(user=owner_query))
        return queryset
