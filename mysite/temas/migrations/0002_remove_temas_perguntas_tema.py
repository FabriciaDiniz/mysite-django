# Generated by Django 2.1.4 on 2019-01-08 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temas',
            name='perguntas_tema',
        ),
    ]
