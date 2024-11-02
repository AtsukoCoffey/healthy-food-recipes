from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`
    """
    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE, default='0'
    )
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
    prep_time = models.IntegerField(default="15")
    cook_time = models.IntegerField(default="40")

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.post.header}: {self.rating}"

    

