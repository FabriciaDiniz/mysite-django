from django.db import models

class Temas(models.Model):
    tema_text = models.CharField(primary_key=True, max_length=200)
    
    def __str__(self):
        return self.tema_text
