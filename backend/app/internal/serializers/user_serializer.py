from app.internal.serializers.image_serializer import ImageSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    picture_detail = ImageSerializer(source="picture", read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "date_joined",
            "is_admin",
            "is_staff",
            "is_active",
            "is_verified",
            "picture",
            "picture_detail",
        ]

        read_only_fields = [
            "id",
            "email",
            "date_joined",
            "is_admin",
            "is_staff",
            "is_active",
            "is_verified",
        ]
        extra_kwargs = {"picture": {"required": False}}
