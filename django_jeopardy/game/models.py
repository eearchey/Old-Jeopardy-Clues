from django.db import models
from django.db.models.aggregates import Count
from random import randint

class clues(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    episode = models.TextField()
    airdate = models.TextField()
    round = models.TextField()
    category = models.TextField()
    worth = models.TextField()
    clue = models.TextField()
    answer = models.TextField()