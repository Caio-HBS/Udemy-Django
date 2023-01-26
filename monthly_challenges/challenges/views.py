from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect
)

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
    'december': "Learn Django for at least 20 minutos a day!",
}


def monthly_challenge_by_number(request, month):
    if month > 0 and month <= 12:
        months_list = list(monthly_challenges_dict.keys())
        redirect_month = months_list[month - 1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    else:
        return HttpResponseNotFound("This month is not valid!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not valid!")
