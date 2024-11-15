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
        lowsugar = self.request.GET.get('lowsugar')
        glutenfree = self.request.GET.get('glutenfree')
        dairyfree = self.request.GET.get('dairyfree')
        vegan = self.request.GET.get('vegan')
        vegitarian = self.request.GET.get('vegitarian')
        highfiber = self.request.GET.get('highfiber')
        highprotein = self.request.GET.get('highprotein')
        nutfree = self.request.GET.get('nutfree')
        avoid_query = self.request.GET.get('q-avoid')
        include_query = self.request.GET.get('q-incl')
        owner_query = self.request.GET.get('q-owner')
        free_query = self.request.GET.get('q-free')
        
        def lowsugar():
            recipes = recipes.filter(lowsugar=True)
        
        def glutenfree():
            recipes = recipes.filter(glutenfree=True)
        
        def dairyfree():
            recipes = recipes.filter(dairyfree=True)
        
        def vegan():
            recipes = recipes.filter(vegan=True)
        
        def vegitarian():
            recipes = recipes.filter(vegitarian=True)
        
        def highfiber():
            recipes = recipes.filter(highfiber=True)
        
        def highprotein():
            recipes = recipes.filter(highprotein=True)
        
        def nutfree():
            recipes = recipes.filter(nutfree=True)
 
        if lowsugar:
            lowsugar()
        if glutenfree:
            glutenfree()
        if dairyfree:
            dairyfree()
        if vegan:
            vegan()
        if vegitarian:
            vegitarian()
        if highfiber:
            highfiber()
        if highprotein:
            highprotein()
        if nutfree:
            nutfree()
        
        return recipes