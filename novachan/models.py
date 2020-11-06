from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, related_name='post_id')
    datetime = models.DateTimeField(auto_now=True)
