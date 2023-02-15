from django.urls import path
from . import views

urlpatterns = [
    # The .as_view() method  points at the  view  class  using it so that Django 
    # treats it as a simple view function.
    path("", views.ReviewView.as_view()),
    path("thank-you", views.thank_youView.as_view()),
    path("reviews", views.reviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.singleReviewView.as_view())
]
