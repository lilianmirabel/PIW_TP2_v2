from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from films.forms import AjoutFilmsForm, AjoutSceanceForm, ReserveSceanceForm, ModifierSceanceForm, ModifierFilmForm
from films.models import salles, films, Seance
from datetime import timedelta, datetime
from datetime import time

def ajoutFilm(request):
    if request.method == "POST":
        form = AjoutFilmsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/administrateur/ajoutfilm")
    else:
        form = AjoutFilmsForm()
    return render(request, "ajoutFilm.html", {'form':form})



def ajoutsceance(request):
    if request.method == "POST":
        form = AjoutSceanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/administrateur/ajoutsceance")
    else:
        form = AjoutSceanceForm()
    return render(request, "ajoutSceance.html", {'form': form})


def ModifierSceance(request, pk):
    uneSceance = Seance.objects.get(id=pk) 
    print(uneSceance)
    if request.method == "POST":
        form = ModifierSceanceForm(request.POST, instance=uneSceance)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect("/films/affiche#")
    else:
        form = ModifierSceanceForm(instance=uneSceance)
    return render(request, 'modifSceance.html', {'form': form})

def Modifierfilm(request, pk):
    unFilm = films.objects.get(titre=pk) 
    print(unFilm)
    if request.method == "POST":
        form = ModifierFilmForm(request.POST, instance=unFilm)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect("/films/affiche#")
    else:
        form = ModifierFilmForm(instance=unFilm)
    return render(request, 'modifFilm.html', {'form': form})

def SupprimerFilm(request, pk):
    films.objects.get(titre=pk).delete()
    return HttpResponseRedirect("/films/affiche#")

def SupprimerSceance(request, pk):
    Seance.objects.get(id=pk).delete()
    return HttpResponseRedirect("/films/affiche#")