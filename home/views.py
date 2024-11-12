from django.views.generic import ListView
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
        return self.model.objects.all()