from django.conf import settings
from django.db import models


def upload_image(instance: "Image", filename: str):
    return f"{instance.name}/{instance.name}.{filename.split('.')[-1]}"


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name="имя", default="default")
    image = models.ImageField(upload_to=upload_image, verbose_name="изображение")

    def __str__(self):
        return self.name
