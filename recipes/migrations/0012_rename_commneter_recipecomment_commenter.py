# Generated by Django 4.2.16 on 2024-11-21 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_recipecomment_alter_recipe_cook_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipecomment',
            old_name='commneter',
            new_name='commenter',
        ),
    ]