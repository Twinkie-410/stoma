from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="заголовок")
    text = models.TextField(verbose_name="текст")
    images = models.ManyToManyField("Image", verbose_name="изображения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def delete(self, using=None, keep_parents=False):
        for image in self.images.all():
            if image.article_set.count() <= 1:
                image.delete()
        return super().delete(using, keep_parents)
