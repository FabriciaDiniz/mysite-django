# Generated by Django 2.1.4 on 2018-12-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('tema_text', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'temas',
            },
        ),
    ]