from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, Submit
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """form to create a recipe"""
    ingredients = forms.CharField(widget=SummernoteWidget())
    instructions = forms.CharField(widget=SummernoteWidget())
    prep_time = forms.IntegerField(label=(u'Preparation time (min)'))
    cook_time = forms.IntegerField(label=(u'Cooking time (min)'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                "Create New Recipe!!",
                "title",
                "description",
                "ingredients",
                "instructions",
                "image",
                "image_alt",
            ),
            Div(
                "prep_time",
                "cook_time",
                css_class='flex-row-form'
            ),
            Div(
                'lowsugar',
                'glutenfree',
                'dairyfree',
                'vegan',
                'vegitarian',
                'highfiber',
                'highprotein',
                'nutfree',
                css_class='flex-row-form'
            ),
            Div(
                Submit('submit', 'Save', wrapper_class='flex-row-form', css_class='btn btn-success col-4'),
                css_class='text-center'
            )
        )
        
    class Meta:
        model = Recipe
        fields = ["title",
                "description",
                "ingredients",
                "instructions",
                "image",
                "image_alt",
                "prep_time",
                "cook_time",
                'lowsugar',
                'glutenfree',
                'dairyfree',
                'vegan',
                'vegitarian',
                'highfiber',
                'highprotein',
                'nutfree',] 
        
