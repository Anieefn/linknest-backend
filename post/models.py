from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=25, default='default_name')
    picture = models.ImageField(upload_to='images/', default='defaults/default_profile.jpg')  # Set the default image
    bio = models.TextField()
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username