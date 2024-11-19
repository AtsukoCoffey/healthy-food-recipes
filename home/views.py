from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.models import User
from recipes.models import Recipe


class Index(ListView):
    """
    Display the list of the recipes
    **Template:**
    :template:`home/index.html` 
    **Context**
    ``recipes`` All recipes :model:`recipes.Recipe`
    ``queryset`` All queried recipes - get_queryset()
    ``all_users`` All users data for option search display
    """
    template_name = 'home/index.html'
    ordering = ['posted_date']
    context_object_name = 'recipes'
    paginate_by = 9
    queryset = Recipe.objects.all()
    print('ASSIGNED QUERYSET: ', queryset)

    # For owner search, send all the User model's name and pk
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add GET parameters to context
        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page') 
        context['query_string'] = query_params.urlencode()
        # All user's data
        context['all_users'] = User.objects.all()
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
        print('REDEFINED QUERYSET: ', queryset)
        
        # 8 checkboxs all the combination query
        # Save the "on" checkbox field in `filters` dictionary
        filters = {}
        for field in ['lowsugar', 'glutenfree', 'dairyfree', 'vegan', 'vegitarian', 'highfiber', 'highprotein', 'nutfree']:
            if self.request.GET.get(field):
                filters[field] = True
        # The filter dictionary goes in the kwargs as like `lowsugar=True` 
        if filters:
            print('FILTERS: ', filters)
            queryset = queryset.filter(**filters)
            print('FILTERED QUERYSET: ', queryset)
        ## pagination issue ========================================================> address later

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
            print('FREE QUERYSET: ', queryset)

        # Owner search 
        if owner_query:
            queryset = queryset.filter(Q(user=owner_query))
        
        print('BEFORE RETURN: ', queryset)
        return queryset