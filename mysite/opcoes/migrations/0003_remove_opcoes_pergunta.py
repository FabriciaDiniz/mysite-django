# Generated by Django 2.1.4 on 2019-05-16 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opcoes', '0002_opcoes_pergunta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcoes',
            name='pergunta',
        ),
    ]
