from django.views import View
from django.shortcuts import render
from novachan.models import *


# Create your views here.
class MainView(View):

    def get(self, request):

        topics = Topic.objects.all()
        return render(request, 'novachan/index.html', {'topics': topics})


class TopicView(View):

    def get(self, request, url):

        topic = Topic.objects.get(url=url)
        threads = Thread.objects.filter(topic_id=topic)
        return render(request, 'novachan/topic.html', {'threads': threads, 'topic': topic})
