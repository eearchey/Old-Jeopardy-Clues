from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='game-home'),
    path('endless_mode/', views.endless_mode, name = 'game-endless_mode'),
    path('episode_mode/', views.episode_years, name = 'game-years'),
    path('episode_mode/<int:year>/', views.episode_months, name='game-months'),
    path('episode_mode/<int:year>/<int:month>', views.episode_episodes, name = 'game-episodes'),
    path('episodes_mode/<int:year>/<int:month>/<int:episode>', views.episode_mode, name = 'game-episode_mode')
]