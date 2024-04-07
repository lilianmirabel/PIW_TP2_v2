from django import forms

from films.models import films, Seance, salles
from django.forms import ModelChoiceField

class AjoutFilmsForm(forms.ModelForm):
    class Meta:
        model = films
        fields = "__all__"
        labels = {'titre':"Titre du Film",
                  'realisateur':"Realisateur du film",
                  'date_sortie':"Date de sortie",
                  'duree':"Durée du film",
                  'resume':"Résumé du film",
                  'image':"Image du film",
                  'genre':"Catégorie du film",
                  }
        widgets = {
            'date_sortie': forms.DateInput(attrs={'type': 'date'}),
            'duree': forms.TimeInput(attrs={'type': 'time'}),
        }



class AjoutSceanceForm(forms.ModelForm):
    # salle = ModelChoiceField(queryset=salles.objects.filter(technologie__in=films.objects.values('technologie')))
    
    class Meta:
        model = Seance
        exclude = ['places_vendues']
        labels = {
            'film': 'Film',
            'salle': 'Salle (Selon la technologie compatible)',
            'heure_diffusion': 'Heure de diffusion',
            'date': 'Date de la séance',
        }
        widgets = {
            'heure_diffusion': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReserveSceanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['places_vendues']
        labels = {
            'places_vendues': 'nombre de place',
        }
        widgets = {
            'places_vendues': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 1, 'value': 1, 'default': 1}),
        }

class ModifierSceanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = "__all__"
        labels = {
            'film': 'Film',
            'salle': 'Salle',
            'heure_diffusion': 'Heure de diffusion',
            'date': 'Date de la séance',
            'places_vendues': 'Nombre de places disponibles'
        }
        widgets = {
            'heure_diffusion': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'places_vendues': forms.NumberInput(attrs={'type': 'number'}),
        }

class ModifierFilmForm(forms.ModelForm):
    class Meta:
        model = films
        fields = "__all__"
        labels = {'titre':"Titre du Film",
                  'realisateur':"Realisateur du film",
                  'date_sortie':"Date de sortie",
                  'duree':"Durée du film",
                  'resume':"Résumé du film",
                  'image':"Image du film",
                  'genre':"Catégorie du film",
                  }
        widgets = {
            'date_sortie': forms.DateInput(attrs={'type': 'date'}),
            'duree': forms.TimeInput(attrs={'type': 'time'}),
        }