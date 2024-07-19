from app.internal.views.topic_view import (
    MyTopicListAPIView,
    TopicCreateAPIView,
    TopicDetailAPIView,
    TopicListAPIView,
    TopicRetrieveAPIView,
)
from django.urls import path

urlpatterns = [
    path("create/", TopicCreateAPIView.as_view(), name="topic-create"),
    path("detail/<int:id>/", TopicDetailAPIView.as_view(), name="topic-detail"),
    path("retrieve/<int:id>/", TopicRetrieveAPIView.as_view(), name="topic-retrieve"),
    path("list/", TopicListAPIView.as_view(), name="topic-list"),
    path("my/", MyTopicListAPIView.as_view(), name="my-topic-list"),
]
