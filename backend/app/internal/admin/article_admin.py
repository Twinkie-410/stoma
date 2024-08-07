from app.internal.models.article_model import Article
from django.contrib import admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
