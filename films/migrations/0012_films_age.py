# Generated by Django 5.0.1 on 2024-04-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_alter_seance_heure_diffusion'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='age',
            field=models.CharField(choices=[('enfant', 'Enfant'), ('adulte', 'Adulte')], default='adulte', max_length=10),
        ),
    ]
