from django.contrib import admin
from novachan.models import *

# Register your models here.
class TopicAdmin(admin.ModelAdmin):

    pass

class PostAdmin(admin.ModelAdmin):

    pass

admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
