from app.internal.models.topic_model import Topic
from django.contrib import admin


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
