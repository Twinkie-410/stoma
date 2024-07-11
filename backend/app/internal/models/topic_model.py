from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    tittle = models.CharField(max_length=255, verbose_name="заголовок")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name="автор")
    created_at = models.DateField(auto_now_add=True, verbose_name="создано")

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = "тема"
        verbose_name_plural = "темы"
