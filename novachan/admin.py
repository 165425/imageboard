from django.contrib import admin
from novachan.models import *


# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    pass


class ReplyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply, ReplyAdmin)
