from app.internal.models.topic_model import Topic
from app.internal.serializers.post_serializer import PostSerializer
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
        read_only_fields = ["created_at", "author"]

    def save(self, **kwargs):
        request = self.context.get("request", None)
        if request:
            self.validated_data["author"] = request.user
        return super().save()


class TopicDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(source="post_set", read_only=True, many=True)

    class Meta:
        model = Topic
        fields = ["id", "tittle", "posts", "author", "created_at"]
        read_only_fields = ["id", "author", "created_at"]
