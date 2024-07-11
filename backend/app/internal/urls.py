from django.urls import include, path

urlpatterns = [
    path("users/", include("app.internal.urls-paths.user_urls")),
    path("auth/", include("app.internal.urls-paths.auth_urls")),
    path("article/", include("app.internal.urls-paths.article_urls")),
    path("image/", include("app.internal.urls-paths.image_urls")),
    path("topic/", include("app.internal.urls-paths.topic_urls")),
    path("post/", include("app.internal.urls-paths.post_urls")),
]
