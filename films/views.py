from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from films.forms import AjoutFilmsForm, AjoutSceanceForm, ReserveSceanceForm
from .models import films, Seance, salles
from datetime import datetime, timedelta

from django.views.generic import ListView, DetailView, CreateView, UpdateView


# def afficheFilm(request):
#     return render(request, "listeFilms.html", {'films':films.objects.all()})

class afficheFilm(ListView):
    model = films
    template_name = "listeFilms.html"
    context_object_name = 'films'


class detailFilm(DetailView):
    model = films
    template_name = "detailFilm.html"
    context_object_name = 'unFilm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unFilm = self.get_object()
        seances = unFilm.seance_set.all()

        # Calculate the number of remaining places for each session
        for seance in seances:
            seance.places_restantes = seance.salle.place - seance.places_vendues
        
        context['seances'] = seances
        return context


class DetailSeance(DetailView):
    model = Seance
    template_name = "detailSceance.html"
    context_object_name = 'uneSceance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uneSceance = self.get_object()

        # Calculate remaining places for the session
        uneSceance.places_restantes = uneSceance.salle.place - uneSceance.places_vendues

        # Calculate end time of the session
        heure_diffusion_dt = datetime.combine(datetime.min, uneSceance.heure_diffusion)
        duree_film_dt = datetime.combine(datetime.min, uneSceance.film.duree)
        heure_fin_dt = heure_diffusion_dt + (duree_film_dt - datetime.min)
        heure_fin = heure_fin_dt.time()

        context['heure_fin'] = heure_fin
        return context

class reserverSceance(UpdateView):
    model = Seance
    template_name = "reserverSceance.html"
    form_class = ReserveSceanceForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.places_vendues += 1
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return '/films/affiche' 


