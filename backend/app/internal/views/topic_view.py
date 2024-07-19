from app.internal.models.topic_model import Topic
from app.internal.serializers.topic_serializer import TopicDetailSerializer, TopicSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class TopicListAPIView(ListAPIView):
    serializer_class = TopicSerializer
    permission_classes = [AllowAny]
    queryset = Topic.objects.all()


class MyTopicListAPIView(ListAPIView):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Topic.objects.filter(author=self.request.user)


class TopicRetrieveAPIView(RetrieveAPIView):
    serializer_class = TopicDetailSerializer
    permission_classes = [AllowAny]
    queryset = Topic.objects.all()
    lookup_field = "id"


class TopicDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Topic.objects.filter(author=self.request.user)


class TopicCreateAPIView(CreateAPIView):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
