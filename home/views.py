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
        
        # 8 checkboxs all the combination
        recipes = Recipe.objects.all()
        if lowsugar:
            if glutenfree:
                if dairyfree:
                    if vegan:
                        if vegitarian:
                            if highfiber:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True).filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True).filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True)
                                else:
                                    recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True).filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True)
                            else:
                                recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True).filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True)
                        else:
                            recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True).filter(
                                        dairyfree=True).filter(vegan=True
                                        )
                    else:
                        recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True).filter(
                                        dairyfree=True)
                else:
                    recipes = recipes.filter(lowsugar=True
                                        ).filter(glutenfree=True)
            else:
                recipes = recipes.filter(lowsugar=True)
        else:
            if glutenfree:
                if dairyfree:
                    if vegan:
                        if vegitarian:
                            if highfiber:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(
                                        glutenfree=True).filter(dairyfree=True
                                        ).filter(vegan=True).filter(
                                        vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(
                                        glutenfree=True).filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True)
                                else:
                                    recipes = recipes.filter(glutenfree=True
                                    ).filter(dairyfree=True).filter(vegan=True
                                    ).filter(vegitarian=True).filter(
                                    highfiber=True)
                            else:
                                recipes = recipes.filter(glutenfree=True
                                    ).filter(dairyfree=True).filter(vegan=True
                                    ).filter(vegitarian=True)
                        else:
                            recipes = recipes.filter(glutenfree=True).filter(
                                dairyfree=True).filter(vegan=True)
                    else:
                        recipes = recipes.filter(glutenfree=True).filter(
                            dairyfree=True)
                else:
                    recipes = recipes.filter(glutenfree=True)
            else:
                if dairyfree:
                    if vegan:
                        if vegitarian:
                            if highfiber:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True)
                                else:
                                    recipes = recipes.filter(
                                        dairyfree=True).filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True)
                            else:
                                recipes = recipes.filter(dairyfree=True
                                ).filter(vegan=True).filter(vegitarian=True)
                        else:
                            recipes = recipes.filter(dairyfree=True
                                ).filter(vegan=True)
                    else:
                        recipes = recipes.filter(dairyfree=True)
                else:
                    if vegan:
                        if vegitarian:
                            if highfiber:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True)
                                else:
                                    recipes = recipes.filter(vegan=True
                                        ).filter(vegitarian=True).filter(
                                        highfiber=True)
                            else:
                                recipes = recipes.filter(vegan=True).filter(
                                    vegitarian=True)
                        else:
                            recipes = recipes.filter(vegan=True)
                    else:
                        if vegitarian:
                            if highfiber:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(
                                        vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(
                                        vegitarian=True).filter(
                                        highfiber=True).filter(
                                        highprotein=True)
                                else:
                                    recipes = recipes.filter(vegitarian=True
                                    ).filter(highfiber=True)
                            else:
                                recipes = recipes.filter(vegitarian=True)
                        else:
                            if highfiber:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(
                                        highfiber=True).filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(
                                        highfiber=True).filter(
                                        highprotein=True)
                                else:
                                    recipes = recipes.filter(
                                        highfiber=True)
                            else:
                                if highprotein:
                                    if nutfree:
                                        recipes = recipes.filter(
                                        highprotein=True).filter(nutfree=True)
                                    else:
                                        recipes = recipes.filter(highprotein=True)

        # Avoid and include query
        if avoid_query:
            if include_query:
                recipes = self.model.objects.all().exclude(
                    ingredients__contains=avoid_query).filter(
                    Q(ingredients__icontains=include_query))
            else:
                recipes = self.model.objects.all().exclude(
                    ingredients__contains=avoid_query)
        else:
            if include_query:
                recipes = self.model.objects.all().filter(
                    Q(ingredients__icontains=include_query))


        return recipes 


