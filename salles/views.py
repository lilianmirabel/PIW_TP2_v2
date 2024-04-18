from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

from salles.forms import AjoutSallesForm, ModifierSalleForm
from films.models import salles


class ajoutSalle(CreateView):
    template_name = 'ajoutSalle.html'
    form_class = AjoutSallesForm 

    def get_success_url(self):
        return reverse('afficheFilm')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Ajouter'
        return context



class listeSalle(ListView):
    model = salles
    template_name = "listeSalles.html"
    context_object_name = 'salles'

class modifierSalle(UpdateView):
    model = salles
    template_name = 'modifierSalle.html'
    form_class = ModifierSalleForm
    context_object_name = 'uneSalle'

    def get_success_url(self):
        return reverse('listeSalle')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Modifier'
        return context

class supprimerSalle(DeleteView):
    model = salles
    template_name = 'supprimerSalle.html'
    context_object_name = 'uneSalle'

    def get_success_url(self):
        return reverse('listeSalle')
