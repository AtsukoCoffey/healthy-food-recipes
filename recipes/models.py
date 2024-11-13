from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.utils.text import slugify


class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`
    """
    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE, default='0'
    )
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    slug = models.SlugField()
    description = models.TextField(max_length=400, null=False, blank=False)
    prep_time = models.IntegerField(default="15")
    cook_time = models.IntegerField(default="40")
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
    lowsugar = models.BooleanField(
        default=False, help_text='e.g. sucrose, glucose, fructose, maltose,\
        fruit juice, molasses, hydrolysed starch, invert sugar, corn syrup,\
        honey etc.')
    glutenfree = models.BooleanField(default=False, help_text='e.g. Wheat,\
        Varieties and derivatives of wheat such as: Rye, Barley, Triticale.')
    dairyfree = models.BooleanField(default=False, help_text='Dairyfree,\
        e.g. Milk, Yogurt, Cheese, lactose-free milk')
    vegitarian = models.BooleanField(default=False, help_text='Pescatarian,\
        Vegitarian, no animal meat except sea-food, eggs and dairy')
    vegan = models.BooleanField(default=False, help_text='Vegan,\
        no animal meat, no exception')
    highfiber = models.BooleanField(default=False, help_text='High-Fiber Food,\
        e.g. Avocado, Artichoke, Lentils, Apple, Beans, Chickpea etc..')
    highprotein = models.BooleanField(default=False, help_text='e.g. Fish,\
        Seafood, White-meat poultry, Lean beef, Dairy, Eggs, Nuts etc..')
    nutfree = models.BooleanField(default=False, help_text='All kind of Nuts.\
        Not include seeds: sesame, sunflower pumpkin, macadamia nut, pine nut')


    def average_rating(self) -> float:
        return Rating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"] or 0

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return f" {self.title}"
        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Recipe,self).save(*args,**kwargs)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.recipe.title}: {self.rating}"

    

