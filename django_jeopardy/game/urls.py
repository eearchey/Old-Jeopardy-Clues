from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='game-home'),
    path('endless_mode/', views.endless_mode, name = 'game-endless_mode'),
    path('years/', views.years, name = 'game-years'),
    path('months/', views.months, name = 'game-months'),
    path('episodes/', views.episodes, name = 'game-episodes'),
    path('episode_mode/', views.episode_mode, name = 'game-episode_mode')
]