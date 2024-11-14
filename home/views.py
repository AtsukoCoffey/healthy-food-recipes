from django.views.generic import ListView
from django.db.models import Q
from  django.contrib.auth.models import User
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
                    ingredients__contains=avoid_query).filter(
                    Q(ingredients__icontains=include_query))
            else:
                queryset = self.model.objects.all().exclude(
                    ingredients__contains=avoid_query)
        else:
            if include_query:
                queryset = self.model.objects.all().filter(
                    Q(ingredients__icontains=include_query))

        return queryset