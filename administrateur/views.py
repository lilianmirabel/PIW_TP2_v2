from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from films.forms import AjoutFilmsForm, AjoutSceanceForm, ReserveSceanceForm, ModifierSceanceForm, ModifierFilmForm
from films.models import salles, films, Seance
from datetime import timedelta, datetime
from datetime import time
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ajoutFilm(CreateView):
    template_name = 'ajoutFilm.html'
    form_class = AjoutFilmsForm 

    def get_success_url(self):
        return reverse('afficheFilm')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Ajouter'
        return context


class ajoutsceance(CreateView):
    template_name = 'ajoutSceance.html'
    form_class = AjoutSceanceForm
    success_url = reverse_lazy('afficheFilm')

    def form_valid(self, form):
        salle = form.cleaned_data['salle']
        heure_debut = form.cleaned_data['heure_diffusion']
        duree_film = form.cleaned_data['film'].duree
        date = form.cleaned_data['date']
        
        heure_debut_datetime = datetime.combine(datetime.today(), heure_debut)
        heure_fin = heure_debut_datetime + timedelta(hours=duree_film.hour, minutes=duree_film.minute)
        
        seances_existantes = Seance.objects.filter(salle=salle, date=date)
        
        conflit = False
        for seance in seances_existantes:
            heure_debut_seance = datetime.combine(datetime.today(), seance.heure_diffusion)
            duree_film_seance = seance.film.duree
            heure_fin_seance = heure_debut_seance + timedelta(hours=duree_film_seance.hour, minutes=duree_film_seance.minute + 30)
            
            if (heure_debut_datetime.time() <= heure_debut_seance.time() < heure_fin.time()) or (heure_debut_seance.time() <= heure_debut_datetime.time() < heure_fin_seance.time()):
                conflit = True
                break
        
        if conflit or form.cleaned_data['film'].technologie != salle.technologie:
            if conflit:
                print("La salle est déjà réservée à cette date et heure.")
            else:
                print("La technologie du film ne correspond pas à celle de la salle.")
            return self.form_invalid(form)
        
        return super().form_valid(form)

class ModifierSceance(UpdateView):
    model = Seance
    template_name = 'modifSceance.html'
    form_class = ModifierSceanceForm
    context_object_name = 'uneSceance'

    def get_success_url(self):
        return reverse('afficheFilm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Modifier'
        return context

class Modifierfilm(UpdateView):
    model = films
    template_name = 'modifFilm.html'
    form_class = ModifierFilmForm
    context_object_name = 'unFilm'

    def get_success_url(self):
        return reverse('afficheFilm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Modifier'
        return context

class SupprimerFilm(DeleteView):
    model = films
    template_name = 'supprimerFilm.html'
    context_object_name = 'unFilm'

    def get_success_url(self):
        return reverse('afficheFilm')

class SupprimerSceance(DeleteView):
    model = Seance
    template_name = 'supprimerSeance.html'
    context_object_name = 'uneSeance'

    def get_success_url(self):
        return reverse('afficheFilm')