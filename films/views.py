from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from films.forms import AjoutFilmsForm, AjoutSceanceForm, ReserveSceanceForm
from .models import films, Seance, salles
from datetime import datetime, timedelta
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View

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

        uneSceance.places_restantes = uneSceance.salle.place - uneSceance.places_vendues
        print(uneSceance.places_restantes)
        
        heure_diffusion_dt = datetime.combine(datetime.min, uneSceance.heure_diffusion)
        duree_film_dt = datetime.combine(datetime.min, uneSceance.film.duree)
        heure_fin_dt = heure_diffusion_dt + (duree_film_dt - datetime.min)
        heure_fin = heure_fin_dt.time()

        uneSceance.places_restantes = uneSceance.salle.place - uneSceance.places_vendues
        
        context['uneSceance'] = uneSceance
        context['heure_fin'] = heure_fin
        return context

class reserverSceance(View):
    def post(self, request, *args, **kwargs):
        une_sceance = get_object_or_404(Seance, pk=self.kwargs['pk'])
        une_sceance.places_vendues += 1
        une_sceance.save()
        return HttpResponseRedirect(('afficheFilm'))


