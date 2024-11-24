from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, Submit
from .models import Post


class PostForm(forms.ModelForm):
    """
    form to create a post with summernote
    """
    post_body = forms.CharField(widget=SummernoteWidget())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                "Create New Post!!",
                "title",
                'image',
                'post_body',
            ),
            Div(
                Submit('submit', 'Save', wrapper_class='flex-row-form', css_class='btn btn-success col-4'),
                css_class='text-center'
            )
        )
    class Meta:
        model = Post
        fields = ['title', 'image', 'post_body',]
        