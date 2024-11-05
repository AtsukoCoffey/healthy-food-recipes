from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """form to create a recipe"""

    class Meta:
        model = Recipe
        widjets = {
            'ingredients' : SummernoteWidget(),
            'instructions' : SummernoteInplaceWidget(),
        }
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "prep_time",
            "cook_time",
            "lowsugar",
            "glutenfree",
            "dairyfree",
            "vegan",
            "vegitarian",
            "highfiber",
            "highprotein",
            "nutfree",
        ]


        