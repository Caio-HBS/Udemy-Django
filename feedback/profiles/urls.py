<<<<<<< HEAD
from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfilesView.as_view())
=======
from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfilesView.as_view())
>>>>>>> 7db6920b4a9d41e78a548ec5f18a2925d35d29e3
]