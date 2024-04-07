from django.urls import path
from administrateur.views import ajoutFilm, ajoutsceance, ModifierSceance, Modifierfilm, SupprimerFilm, SupprimerSceance

urlpatterns = [
    path('ajoutfilm', ajoutFilm, name="ajoutFilm"),
    path('ajoutsceance', ajoutsceance, name="ajoutsceance"),
    path('ModifierSceance/<str:pk>/', ModifierSceance, name="ModifierSceance"),
    path('SupprimerSceance/<str:pk>/', SupprimerSceance, name="SupprimerSceance"),
    path('Modifierfilm/<str:pk>/', Modifierfilm, name="Modifierfilm"),
    path('SupprimerFilm/<str:pk>/', SupprimerFilm, name="SupprimerFilm"),
]