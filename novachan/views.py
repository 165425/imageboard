from django.views import View
from django.shortcuts import render
from novachan.models import *
from novachan.forms import *


# Create your views here.
class MainView(View):

    def get(self, request):

        topics = Topic.objects.all()
        return render(request, 'novachan/index.html', {'topics': topics})


class TopicView(View):

    def get(self, request, url):
        topic = Topic.objects.get(url=url)
        threads = Thread.objects.filter(topic_id=topic)
        replies = Reply.objects.filter(thread_id__in=threads)

        form = SubmitPostForm()  # Generate empty form
        return render(request, 'novachan/topic.html', {
            'threads': threads,
            'topic': topic,
            'replies': replies,
            'form': form
        })

    # def post(self, request):
    #     form = SubmitPostForm(request.POST)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         pass
    #         #  return self.form_invalid(form)  # TODO this
    #
    # def form_valid(self, form):
    #     name = form.cleaned_data['name']
    #     text = form.cleaned_data['text']
    #     image = form.cleaned_data['image']
