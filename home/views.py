from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.models import User
from recipes.models import Recipe


class Index(ListView):
    """
    Display the list of the recipes :model:`recipes.Recipe`.
    **Template:**
    :template:`home/index.html` 
    """
    template_name = 'home/index.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 9

    # For owner search, send all the User model's name and pk
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_users'] = User.objects.all()
        return context

    def get_queryset(self):
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
        for field in ['lowsugar', 'glutenfree', 'dairyfree', 'vegan', 'vegitarian', 'highfiber', 'highprotein', 'nutfree']:
            if self.request.GET.get(field):
                filters[field] = True
        # The filter dictionary goes in the kwargs as like `lowsugar=True` 
        if filters:
            queryset = queryset.filter(**filters)
        ## pagination issue ========================================================> address later

        # Avoid and include Ingredients query
        if avoid_query:
            if include_query:
                queryset = self.model.objects.all().exclude(
                    ingredients__icontains=avoid_query).filter(
                    Q(ingredients__icontains=include_query))
            else:
                queryset = self.model.objects.all().exclude(
                    ingredients__icontains=avoid_query)
        else:
            if include_query:
                queryset = self.model.objects.all().filter(
                    Q(ingredients__icontains=include_query))
        
        # # Free search in Title, Description, Instruction
        # print(free_query)
        # if free_query:
        #     print(free_query)
        #     queryset = self.model.objects.all().filter(
        #         Q(title__icontains=query) |
        #         Q(description__icontains=query) |
        #         Q(instructions__icontains=query)
        #     )

        

        return queryset