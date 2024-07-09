from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="заголовок")
    text = models.TextField(verbose_name="текст")
    images = models.ManyToManyField("Image", verbose_name="изображения")

    def __str__(self):
        return self.title
