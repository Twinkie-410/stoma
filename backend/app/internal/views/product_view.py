from app.internal.models.product_model import Product
from app.internal.serializers.product_serializer import ProductSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = []
    queryset = Product.objects.all()


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = []
    queryset = Product.objects.all()
    lookup_field = "id"


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = []
