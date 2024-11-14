from django.views.generic import ListView
from django.db.models import Q
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
    recipes = Recipe.objects.all()

    def get_queryset(self):
        """
        Search option modal's query
        8 checkboxes - on or None
        owner_query - int (foreign key)
        others are - string
        """
        queryset = Recipe.objects.all()
        filters = {}
        for field in ['lowsugar', 'glutenfree', 'dairyfree', 'vegan', 'vegitarian', 'highfiber', 'highprotein', 'nutfree']:
            if self.request.GET.get(field):
                filters[field] = True
        if filters:
            queryset = queryset.filter(**filters)
        
        return queryset