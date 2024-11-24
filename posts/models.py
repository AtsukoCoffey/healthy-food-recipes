from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Stores a post entry related to :model:`auth.User`
    """
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    user = models.ForeignKey(
        User, related_name="post_owner", on_delete=models.CASCADE, default='0'
    )
    post_body = models.TextField(max_length=1000, null=False, blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


