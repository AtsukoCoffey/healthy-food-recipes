from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, Submit
from .models import Recipe, RecipeComment


class RecipeForm(forms.ModelForm):
    """
    form to create a recipe with summernote
    """
    ingredients = forms.CharField(widget=SummernoteWidget())
    instructions = forms.CharField(widget=SummernoteWidget())
    prep_time = forms.CharField(label=(u'Preparation time'), required=False)
    cook_time = forms.CharField(label=(u'Cooking time'), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                "Please share your favorite recipes!!!",
                "title",
                "description",
                "ingredients",
                "instructions",
                "image",
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
        widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }
        

class RecipeCommentForm(forms.ModelForm):
    """
    Form to leave a comment on the recipe. :model recipes.RecipeComment
    """
    class Meta:
        model = RecipeComment
        fields = ('comment_body',)
        widgets = {
          'comment_body': forms.Textarea(attrs={'rows':3}),
        }
