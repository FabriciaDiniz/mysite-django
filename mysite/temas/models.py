from django.db import models

class Temas(models.Model):
    tema_text = models.CharField(primary_key=True, max_length=200)
    perguntas_tema = models.ForeignKey('polls.Perguntas', on_delete=models.DO_NOTHING, null=True, default=None)
    
    def __str__(self):
        return self.tema_text

    class Meta:
        db_table = 'temas'