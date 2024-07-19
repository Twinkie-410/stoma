from app.internal.views.article_view import ArticleCreateAPIView, ArticleDetailAPIView, ArticleListAPIView
from django.urls import path

urlpatterns = [
    path("create/", ArticleCreateAPIView.as_view(), name="article-create"),
    path("<int:id>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("list/", ArticleListAPIView.as_view(), name="article-list"),
]
