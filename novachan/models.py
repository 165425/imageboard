from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    url = models.SlugField()

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=True, null=True, default='Anoniem', max_length=100)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Thread(Post):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"thread {self.id}"


class Reply(Post):
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return f"reply {self.id}"
