from app.internal.models.post_model import Post
from app.internal.serializers.image_serializer import ImageSerializer
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    images_detail = ImageSerializer(source="images", read_only=True, many=True)

    class Meta:
        model = Post
        fields = ["id", "topic", "author", "message", "images", "images_detail", "created_at", "post_reply"]
        read_only_fields = ["created_at", "author"]
        extra_kwargs = {"images": {"required": False, "allow_empty": True}}

    def save(self, **kwargs):
        request = self.context.get("request", None)
        if request:
            self.validated_data["author"] = request.user
        return super().save()
