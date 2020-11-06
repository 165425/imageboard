from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Thread(Post):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Reply(Post):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
