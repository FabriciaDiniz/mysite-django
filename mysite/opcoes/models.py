from django.db import models


class Opcoes(models.Model):
    opcao_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao_text

    class Meta:
        db_table = 'opcoes'