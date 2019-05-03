from django.contrib import admin

from mysite.perguntas.models import Perguntas
from mysite.temas.models import Temas
from mysite.opcoes.models import Opcoes

admin.site.register(Temas)
admin.site.register(Perguntas)
admin.site.register(Opcoes)