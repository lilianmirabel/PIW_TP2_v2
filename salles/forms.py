from django import forms

from films.models import salles

class AjoutSallesForm(forms.ModelForm):
    class Meta:
        model = salles
        fields = "__all__"
        labels = {'place':"Nombre de places",
                  'technologie':"Technologie utilisé",
                  'prix_ticket':"Prix du ticket"}

class ModifierSalleForm(forms.ModelForm):
    class Meta:
        model = salles
        fields = "__all__"
        labels = {'place':"Nombre de places",
                  'technologie':"Technologie utilisé",
                  'prix_ticket':"Prix du ticket"}
        widgets = {
            'date_sortie': forms.DateInput(attrs={'type': 'date'}),
            'duree': forms.TimeInput(attrs={'type': 'time'}),
        }