import datetime

from django.db import models
from django.utils import timezone

class Theme(models.Model):
    theme_text = models.CharField(primary_key=True, max_length=200)
    def __str__(self):
        return self.theme_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, default='Fun')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

