from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, PostComment


@admin.register(Post)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'image',
        'post_body',
        'user'
        )
    search_fields = ['title', 'post_body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_body')


admin.site.register(PostComment)
