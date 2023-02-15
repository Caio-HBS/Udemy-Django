from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import (
    ListView, 
    DetailView)
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review


# Class-based  view  that  does  virtually  the same as  functions, but are more 
# powerfull and reduce drastically the amount of code.
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # Handles what to do with a valid form.
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # Yields the exact same  result as the code  seen above, but  using a simple 
    # "View" class.
    # Handle the GET requests, without the need for 'if' checks.
    ##def get(self, request):
        ##form = ReviewForm
        ##return render(request, "reviews/review.html", {
        ##"form": form
    ##})
    # Handle the POST requests, without the need for 'if' checks.
    ##def post(self, request):
        ##form = ReviewForm(request.POST)
        ##if form.is_valid():
            ##form.save()
            ##return HttpResponseRedirect("/thank-you")
        ##else:
            ##form = ReviewForm()
            ##return render(request, "reviews/review.html", {
                ##"form": form
            ##})


# Does virtually the same as the class-based view above, but it's less powerfull 
# and a lot more code heavy.
#def review(request):
    ##if request.method == 'POST':
        # Stores the POST request in the review form initiated in 'forms.py'.
        ##form = ReviewForm(request.POST)
        # Validates the input,  validates the form  itself and returns a boolean
        # and populate another field with the valid data should it be valid.
        ##if form.is_valid():
            ##form.save()
            ##return HttpResponseRedirect("/thank-you")
    # Makes  sure the  recieved  data is  still  stored  even if the  validation 
    # failed.
    ##else:
        ##form = ReviewForm()
    ##return render(request, "reviews/review.html", {
        ##"form": form
    ##})


# Simply deals  with the 'thank you' page  rendering using the built-in template 
# view.
class thank_youView(TemplateView):
    template_name = "reviews/thank_you.html"

    # Get the data from the template so that we can populate fields on it.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

# Handles the 'index' page by reaching for the database and creating a list.
class reviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    # Does the exact same as seen above, except using the TemplateView.
    ##def get_context_data(self, **kwargs):
        ##context = super().get_context_data(**kwargs)
        ##reviews = Review.objects.all()
        ##context["reviews"] = reviews
        ##return context

# Handles  the  'single view' page by  reaching for  the  database and pulling a 
# specific review.
class singleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"

    # Reaches for the session to know if the review is marked favorite or not so
    # that is can show it when loading the review.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Reaches for the review object.
        loaded_review = self.object
        # Reaches for the request.
        request = self.request
        # Tries to get the favorite review key, if it doesn't exist, simply go 
        # about returning the context (meaning show it's not marked as favorite)
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


    # Does the exact same as seen above, except using the TemplateView.
    ##def get_context_data(self, **kwargs):
        ##context = super().get_context_data(**kwargs)
        ##review_id = kwargs["id"]
        ##selected_review = Review.objects.get(pk=review_id)
        ##context["review"] = selected_review
        ##return context

# Handles the favorite function.
class AddFavoriteView(View):
    def post(self, request):
        # Gets the POST request.
        review_id = request.POST["review_id"]
        # Adds the value to the session so that it knows it's marked as favorite
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)