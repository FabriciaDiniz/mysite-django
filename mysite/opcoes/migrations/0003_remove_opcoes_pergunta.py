# Generated by Django 2.1.4 on 2018-12-17 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opcoes', '0002_auto_20181217_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcoes',
            name='pergunta',
        ),
    ]