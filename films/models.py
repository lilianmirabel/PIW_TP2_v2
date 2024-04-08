from django.db import models
import datetime

class salles(models.Model):
    choix_technologies = (
        ('Numérique', 'Numérique'), 
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
        ('4DX', '4DX')
    )

    id = models.AutoField(primary_key=True)
    place = models.IntegerField()
    technologie = models.CharField(max_length=10, choices=choix_technologies)
    prix_ticket = models.FloatField()

    def __str__(self):
        return  str(self.id) + " - " + str(self.technologie)

from django.db import models
import datetime

class films(models.Model):
    AGE_CHOICES = (
        ('enfant', 'Enfant'),
        ('adulte', 'Adulte')
    )

    choix_technologies = (
        ('Numérique', 'Numérique'), 
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
        ('4DX', '4DX')
    )

    titre = models.CharField(max_length=100, primary_key=True)
    realisateur = models.CharField(max_length=100)
    date_sortie = models.DateField(default=datetime.date.today)
    genre = models.CharField(max_length=100)
    resume = models.TextField()
    duree = models.TimeField()
    image = models.CharField(max_length=100)
    age = models.CharField(max_length=10, choices=AGE_CHOICES, default='adulte')
    technologie = models.CharField(max_length=10, choices=choix_technologies, default='Numérique')


    def __str__(self):
        return self.titre


class Seance(models.Model):
    id = models.AutoField(primary_key=True)
    film = models.ForeignKey(films, on_delete=models.CASCADE)
    salle = models.ForeignKey(salles, on_delete=models.CASCADE)
    heure_diffusion = models.TimeField()
    date = models.DateField()
    places_vendues = models.IntegerField(default=0)

    class Meta:
        unique_together = (('salle', 'date', 'heure_diffusion'),)
    

