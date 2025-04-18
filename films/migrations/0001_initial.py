# Generated by Django 5.0.1 on 2024-03-10 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('realisateur', models.CharField(max_length=100)),
                ('annee', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('resume', models.TextField()),
                ('duree', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
