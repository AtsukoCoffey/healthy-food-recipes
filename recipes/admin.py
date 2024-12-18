from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Recipe, Rating, RecipeComment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = (
        'image',
        'title',
        'user',
        'lowsugar',
        'glutenfree',
        'dairyfree',
        'vegan',
        'vegitarian',
        'highfiber',
        'highprotein',
        'nutfree',
        'posted_date'
        )
    search_fields = ['title', 'ingredients']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')


admin.site.register(Rating)

admin.site.register(RecipeComment)
