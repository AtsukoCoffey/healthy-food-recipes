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

    def get_queryset(self, **kwargs):
        avoid_query = self.request.GET.get('q-avoid')
        include_query = self.request.GET.get('q-incl')
        owner_query = self.request.GET.get('q-owner')
        free_query = self.request.GET.get('q-free')

        if avoid_query:
            recipes = self.model.objects.all().exclude(ingredients__contains=avoid_query)
        elif include_query:
            recipes = self.model.objects.filter(
                Q(ingredients__icontains=include_query)
            )
        elif owner_query:
            recipes = self.model.objects.filter(
                Q(user__contains=owner_query)
            )
        elif free_query:
            recipes = self.model.objects.filter(
                Q(description__icontains=free_query) |
                Q(instructions__icontains=free_query) |
                Q(ingredients__icontains=free_query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes