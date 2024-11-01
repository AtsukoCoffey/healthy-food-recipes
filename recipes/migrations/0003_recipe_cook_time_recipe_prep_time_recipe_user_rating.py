# Generated by Django 4.2.16 on 2024-11-02 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_recipe_slug_alter_recipe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(default='40'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(default='15'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='recipe_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
