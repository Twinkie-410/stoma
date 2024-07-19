from app.internal.views.product_view import ProductCreateAPIView, ProductDetailAPIView, ProductListAPIView
from django.urls import path

urlpatterns = [
    path("create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("<int:id>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("list/", ProductListAPIView.as_view(), name="product-list"),
]
