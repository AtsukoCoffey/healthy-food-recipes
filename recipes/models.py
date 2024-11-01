from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`
    """
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, default='title')
    description = models.CharField(max_length=400, null=False, blank=False)
    ingredients = models.TextField(
        max_length=10000, null=False, blank=False, default="Ingredients"
    )
    instructions = models.TextField(
        max_length=10000, null=False, blank=False, default="Instructions"
    )
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)
    lowsugar = models.BooleanField()
    glutenfree = models.BooleanField()
    dairyfree = models.BooleanField()
    vegan = models.BooleanField()
    vegitarian = models.BooleanField()
    highfiber = models.BooleanField()
    highprotein = models.BooleanField()
    nutfree = models.BooleanField()

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)

    

