from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.utils.text import slugify


class Post(models.Model):
    """
    Stores a post entry related to :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    user = models.ForeignKey(
        User, related_name="post_owner", on_delete=models.CASCADE, default='0'
    )
    slug = models.SlugField()
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="posts/",
        force_format="WEBP",
        default='https://res.cloudinary.com/dulfdtcut/image/upload/v1731383533/recipes/Screenshot_2024-10-25_211028_zlqtk7.webp'
    )
    image_alt = models.CharField(max_length=50)
    post_body = models.TextField(max_length=3000, null=False, blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return f" {self.title}"
        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title[0:20])
        self.image_alt=self.title[0:40]
        super(Post,self).save(*args,**kwargs)


class PostComment(models.Model):
    """
    Stores a single comment entry related to :modl:`auth.User`
    and :model:`posts.Post`. 
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_body = models.CharField(max_length=200)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_commenter")
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]