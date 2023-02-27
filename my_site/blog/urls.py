from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="single-post"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
