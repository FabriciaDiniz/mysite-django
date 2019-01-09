from django.db import models

class Temas(models.Model):

    tema_text = models.CharField(max_length=200)
    #existe o campo perguntas_tema, criado no models das perguntas
    
    def __str__(self):
        return self.tema_text

    class Meta:
        db_table = 'temas'