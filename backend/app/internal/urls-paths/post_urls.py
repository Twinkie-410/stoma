from app.internal.views.post_view import PostCreateAPIView, PostDetailAPIView
from django.urls import path

urlpatterns = [
    path("create/", PostCreateAPIView.as_view(), name="post-create"),
    path("detail/<int:id>/", PostDetailAPIView.as_view(), name="post-detail"),
]
