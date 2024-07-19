from django.db import models


class Product(models.Model):
    SINGLE = "Однокомпонентный"
    TWO = "Двухкомпонентный"
    CHILD = "Детский"
    POSTSURGICAL = "Послеоперационный"
    ACCESSORIES = "Аксессуары"
    TYPE_CHOICES = [
        (SINGLE, SINGLE),
        (TWO, TWO),
        (CHILD, CHILD),
        (POSTSURGICAL, POSTSURGICAL),
        (ACCESSORIES, ACCESSORIES),
    ]
    name = models.CharField(max_length=255, verbose_name="название")
    brand = models.CharField(max_length=255, verbose_name="производитель")
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name="тип")
    description = models.TextField(verbose_name="описание")
    images = models.ManyToManyField("Image", verbose_name="изображения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
