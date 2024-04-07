from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from films.forms import AjoutFilmsForm, AjoutSceanceForm, ReserveSceanceForm
from .models import films, Seance, salles
from datetime import datetime, timedelta


# def ajoutFilm(request):
#     if request.method == "POST":
#         form = AjoutFilmsForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect("/films")
#     else:
#         form = AjoutFilmsForm()
#     return render(request, "ajoutFilm.html", {'form':form})

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

# def ajoutsceance(request):
#     if request.method == "POST":
#         form = AjoutSceanceForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect("/films")
#     else:
#         form = AjoutSceanceForm()
#     return render(request, "ajoutSceance.html", {'form':form})


def detailSceance(request, pk):
    uneSceance = Seance.objects.get(id=pk)
    uneSceance.places_restantes = uneSceance.salle.place - uneSceance.places_vendues

    # Convertir l'heure de diffusion et la durée du film en objets datetime
    heure_diffusion_dt = datetime.combine(datetime.min, uneSceance.heure_diffusion)
    duree_film_dt = datetime.combine(datetime.min, uneSceance.film.duree)

    # Calculer l'heure de fin en ajoutant la durée du film à l'heure de diffusion
    heure_fin_dt = heure_diffusion_dt + (duree_film_dt - datetime.min)

    # Extraire l'heure de fin et la convertir en format time
    heure_fin = heure_fin_dt.time()

    return render(request, 'detailSceance.html', {'uneSceance': uneSceance, 'heure_fin': heure_fin})




def reserverSceance(request, pk):
    uneSceance = Seance.objects.get(pk=pk)
    uneSceance.places_vendues += 1
    uneSceance.save()
    return HttpResponseRedirect("/films/affiche#")


