from app.internal.models.article_model import Article
from app.internal.serializers.image_serializer import ImageSerializer
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    images_detail = ImageSerializer(source="images", read_only=True, many=True)

    class Meta:
        model = Article
        fields = ["id", "title", "text", "images", "images_detail"]
        extra_kwargs = {"images": {"required": False, "allow_empty": True}}
