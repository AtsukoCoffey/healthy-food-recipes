# Generated by Django 4.2.16 on 2024-11-06 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_cook_time_recipe_prep_time_recipe_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(),
        ),
    ]