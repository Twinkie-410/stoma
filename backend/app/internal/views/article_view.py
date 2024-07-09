from app.internal.models.article_model import Article
from app.internal.serializers.article_serializer import ArticleSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView


class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = []
    queryset = Article.objects.all()


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = []
    queryset = Article.objects.all()
    lookup_field = "id"


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = []
    queryset = Article.objects.all()
