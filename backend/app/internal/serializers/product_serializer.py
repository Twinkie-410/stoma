from app.internal.models.product_model import Product
from app.internal.serializers.image_serializer import ImageSerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    images_detail = ImageSerializer(source="images", read_only=True, many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "brand", "type", "description", "images", "images_detail"]
        extra_kwargs = {"images": {"required": False, "allow_empty": True}}
