import datetime

from django.db import models
from django.utils import timezone

class Perguntas(models.Model):

    pergunta_text = models.CharField(max_length=200)
    tema = models.ForeignKey('temas.Temas', on_delete=models.CASCADE, null=True, default=None, related_name='perguntas_tema')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.pergunta_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        db_table = 'perguntas'