from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('image', 'title', 'ingredients')
    search_fields = ['title', 'ingredients']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')





