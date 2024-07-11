from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE, verbose_name="тема")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name="автор")
    message = models.TextField(verbose_name="сообщение")
    images = models.ManyToManyField("Image", verbose_name="изображения")
    created_at = models.DateField(auto_now_add=True, verbose_name="создано")
    post_reply = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, verbose_name="ответ")

    def __str__(self):
        return self.message[:50]

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
