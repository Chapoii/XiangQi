from django.urls import path

from chess import views

app_name = "chess"

urlpatterns = [
    path("index", views.Index.as_view(), name="index"),  # 首页
    path("feedback", views.Feedback.as_view(), name="feedback"),
    path("about", views.About.as_view(), name="about"),
]
