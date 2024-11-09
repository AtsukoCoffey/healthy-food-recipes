from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """form to create a recipe"""
    ingredients = forms.CharField(widget=SummernoteWidget())
    instructions = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Recipe
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


        