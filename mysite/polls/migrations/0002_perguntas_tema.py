# Generated by Django 2.1.4 on 2019-01-08 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('temas', '0001_initial'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perguntas',
            name='tema',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='temas.Temas'),
        ),
    ]
