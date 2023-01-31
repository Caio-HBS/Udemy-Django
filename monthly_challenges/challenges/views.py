from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponseNotFound,
    HttpResponseRedirect
)
from django.urls import reverse



monthly_challenges_dict = {
    'january': "Eat no meat for the entire month!",
    'february': "Walk for at least 20 minutes every day!",
    'march': "Learn Django for at least 20 minutos a day!",
    'april': "Eat no meat for the entire month!",
    'may': "Walk for at least 20 minutes every day!",
    'june': "Learn Django for at least 20 minutos a day!",
    'july': "Eat no meat for the entire month!",
    'august': "Walk for at least 20 minutes every day!",
    'september': "Learn Django for at least 20 minutos a day!",
    'october': "Eat no meat for the entire month!",
    'november': "Walk for at least 20 minutes every day!",
    'december': None
}

# Used to handle the main page, creating the index of months, and sending it to 
# the html.
def index(request):
    months = list(monthly_challenges_dict.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

# Used to handle the URLs  constructed with numbers, if the number is not valid, 
# returns a standard 404 response.
def monthly_challenge_by_number(request, month):
    if month > 0 and month <= 12:
        months_list = list(monthly_challenges_dict.keys())
        redirect_month = months_list[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("This month is not valid!")

# Used to handle each one of the months.
def monthly_challenge(request, month):
    # Constructs the  path to the  desired month. If it can't construct, returns 
    # the 404.html.
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        raise Http404()
