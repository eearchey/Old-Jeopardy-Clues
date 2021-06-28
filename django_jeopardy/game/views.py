from django.shortcuts import render
from django.http import HttpResponse
from .models import clues
import random
import calendar
from django.core import serializers
import re
import datetime

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
    grouped_years = []
    for i in range(len(years)):
        if i % 6 == 0:
            grouped_years.append([])
        grouped_years[i//6].append(years[i])
    while len(grouped_years[-1]) < 6:
        grouped_years[-1].append("")
    context = {
        'years': grouped_years
    }
    return render(request, 'game/episode_years.html', context)

def episode_months(request, year):
    episodes = clues.objects.order_by('airdate').distinct('airdate')
    months = []
    nums = []
    episodes = [episode for episode in episodes if episode.airdate[0:4] == str(year)]
    for episode in episodes:
        episode.airdate = episode.airdate[5:7]
        month_name = calendar.month_name[int(episode.airdate)]
        if (episode.airdate, month_name) not in months:
            months.append((episode.airdate, month_name))
    grouped_months = []
    for i in range(len(months)):
        if i % 6 == 0:
            grouped_months.append([])
        grouped_months[i//6].append(months[i])
    while len(grouped_months[-1]) < 6:
        grouped_months[-1].append("")
    context = {
        'months': grouped_months,
        'year': year
    }
    return render(request, 'game/episode_months.html', context)

def episode_dates(request, year, month):
    episodes = clues.objects.order_by('airdate').distinct('airdate')
    month_str = str(month)
    if month < 10:
        month_str = "0" + str(month)
    month_name = calendar.month_name[int(month_str)]
    month_info = [month, month_name]
    episodes = [episode for episode in episodes if episode.airdate[0:4] == str(year) and episode.airdate[5:7] == month_str]
    dates = []
    for episode in episodes:
        date = int(episode.airdate[8:10])
        if date not in dates:
            dates.append(date)
    dates.sort()
    grouped_dates = []
    for i in range(len(dates)):
        if i % 6 == 0:
            grouped_dates.append([])
        grouped_dates[i//6].append(dates[i])
    while len(grouped_dates[-1]) < 6:
        grouped_dates[-1].append("")
    context = {
        'dates': grouped_dates,
        'month': month_info,
        'year': year
    }
    return render(request, 'game/episode_dates.html', context)

def episode_single_board(request, year, month, date):
    month_str = str(month)
    date_str = str(date)
    if month < 10:
        month_str = "0" + month_str
    if date < 10:
        date_str = "0" + date_str
    date_string = str(year) + '-' + str(month_str) + '-' + str(date_str)
    episodes = clues.objects.filter(airdate=date_string, round='Jeopardy!')
    categories = []
    for episode in episodes:
        category = episode.category
        if category not in categories:
            categories.append(category)
            index = categories.index(category)
    categories.sort()
    context = {
        'categories': categories,
        'clues': episodes
    }
    return render(request, 'game/episode_single_board.html', context)

def episode_board(request, year, month, date):
    month_str = str(month)
    date_str = str(date)
    if month < 10:
        month_str = "0" + month_str
    if date < 10:
        date_str = "0" + date_str
    date_string = str(year) + '-' + str(month_str) + '-' + str(date_str)
    episodes = clues.objects.filter(airdate=date_string, round='Jeopardy!')
    categories = {}
    for episode in episodes:
        category = episode.category
        if categories.get(episode.category):
            categories[episode.category].append(episode.id)
        else:
            categories[episode.category] = [episode.id]
    categories = [(k, v) for k, v in categories.items()]
    categories.sort(key=lambda x: x[0])
    context = {
        'categories': categories
    }
    return render(request, 'game/episode_board.html', context)

def episode_question(request):
    qid = request.GET.get('qid')
    episodes = clues.objects.get(id=qid)
    context = {
        'clue': episodes
    }
    return render(request, 'game/episode_question.html', context)