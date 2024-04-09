from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from films.forms import AjoutFilmsForm, AjoutSceanceForm, ReserveSceanceForm
from .models import films, Seance, salles
from datetime import datetime, timedelta

def afficheFilm(request):
    return render(request, "listeFilms.html", {'films':films.objects.all()})

def detailFilm(request, pk):
    unFilm = films.objects.get(titre=pk)
    seances = unFilm.seance_set.all()
    
    # Calculer le nombre de places restantes pour chaque séance
    for seance in seances:
        seance.places_restantes = seance.salle.place - seance.places_vendues
    
    context = {'unFilm': unFilm, 'seances': seances}
    return render(request, 'detailFilm.html', context)


def detailSceance(request, pk):
    uneSceance = Seance.objects.get(id=pk)
    return render(request, 'detailSceance.html', {'uneSceance': uneSceance})




def reserverSceance(request, pk):
    uneSceance = Seance.objects.get(pk=pk)
    uneSceance.places_vendues += 1
    uneSceance.save()
    return HttpResponseRedirect("/films/affiche#")


