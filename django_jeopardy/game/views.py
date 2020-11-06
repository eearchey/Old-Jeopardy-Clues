from django.shortcuts import render
from django.http import HttpResponse
from .models import clues
import random
import calendar
from django.core import serializers
import re

def home(request):
    return render(request, 'game/home.html')

def endless_mode(request):
    random_index = random.randint(4,clues.objects.count() - 1)
    random_obj = clues.objects.all()[random_index]
    random_obj.clue = random_obj.clue.upper()
    airdate = random_obj.airdate.split('-')
    month = calendar.month_name[int(airdate[1])]
    
    suffix = 'th'
    if airdate[2][1] == '1':
        suffix = 'st'
    elif airdate[2][1] == '2':
        suffix = 'nd'
    elif airdate[2][1] == '3':
        suffix = 'rd'
    if airdate[2][0] == '0':
        airdate[2] = airdate[2][1]
    
    random_obj.airdate = month + " " + airdate[2] + suffix + ", " + airdate[0]
    i = '\\'
    random_obj.clue = random_obj.clue.replace(i, '')
    random_obj.category = random_obj.category.replace(i, '')
    random_obj.answer = random_obj.answer.replace(i, '')
    random_obj.worth = random_obj.worth.replace(i, '')
    random_obj.airdate = random_obj.airdate.replace(i, '')
    
    context = {
        'clue': random_obj
    }
    
    return render(request, 'game/endless_mode.html', context)

def episode_years(request):
    episodes = clues.objects.order_by('airdate').distinct('airdate')
    years = []
    for episode in episodes:
        episode.airdate = episode.airdate[0:4]
        if episode.airdate not in years:
            years.append(episode.airdate)
    context = {
        'years': years
    }
    return render(request, 'game/years.html', context)

def episode_months(request):
    request.GET.get('year_choice')
    episodes = clues.objects.order_by('airdate').distinct('airdate')
    months = []
    for episode in episodes:
        episode.airdate = episode.airdate[6:7]
        month = calendar.month_name[int(episode.airdate)]
        if month not in months:
            months.append(month)
    context = {
        'months': months
    }
    return render(request, 'game/months.html', context)

def episode_episodes(request):
    episodes = clues.objects.order_by('airdate').distinct('airdate')
    dates = []
    for episode in episodes:
        date = episode.airdate[9:10]
        if date not in dates:
            dates.append(date)
    context = {
        'dates': date
    }
    return render(request, 'game/episodes.html')

def episode_mode(request):
    return render(request, 'game/episode_mode.html')