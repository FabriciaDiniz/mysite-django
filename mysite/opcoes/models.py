from django.db import models
from mysite.temas.models import Temas

class Opcoes(models.Model):
    pergunta = models.ForeignKey('polls.Perguntas', on_delete=models.CASCADE, null=True, default=None)
    opcao_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.opcao_text

    class Meta:
        db_table = 'opcoes'