# Generated by Django 5.0.1 on 2024-03-21 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_rename_annee_films_date_sortie'),
    ]

    operations = [
        migrations.CreateModel(
            name='salles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.IntegerField()),
                ('technologie', models.CharField(choices=[('Numérique', 'Numérique'), ('3D', '3D'), ('IMAX', 'IMAX'), ('4DX', '4DX')], max_length=10)),
                ('prix_ticket', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='films',
            name='id',
        ),
        migrations.AlterField(
            model_name='films',
            name='date_sortie',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='films',
            name='duree',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='films',
            name='titre',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
