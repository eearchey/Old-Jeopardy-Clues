from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='game-home'),
    path('endless_mode/', views.endless_mode, name = 'game-endless_mode'),
    path('episode_mode/', views.episode_years, name = 'game-episode_years'),
    path('episode_mode/<int:year>/', views.episode_months, name='game-episode_months'),
    path('episode_mode/<int:year>/<int:month>/', views.episode_dates, name = 'game-episode_dates'),
    path('episode_mode/<int:year>/<int:month>/<int:date>/single', views.episode_single_board, name = 'game-episode_single_board'),
    path('episode_mode/<int:year>/<int:month>/<int:date>/board', views.episode_board, name = 'game-episode_board'),
    path('episode_mode/question', views.episode_question, name = 'game-episode_question')
]