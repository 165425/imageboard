from django.views import View
from django.shortcuts import render
from novachan.models import *


# Create your views here.
class MainView(View):

    def get(self, request):

        topics = Topic.objects.all()
        return render(request, 'novachan/index.html', {'topics': topics})


class TopicView(View):

    def get(self, request, id):

        topic = Topic.objects.get(pk=id)
        posts = Post.objects.filter(topic=topic)
        return render(request, 'novachan/topic.html', {'posts': posts, 'topic': topic})
