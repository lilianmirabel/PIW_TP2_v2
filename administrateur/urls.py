from django.urls import path
from administrateur.views import ajoutFilm, ajoutsceance, ModifierSceance, Modifierfilm, SupprimerFilm, SupprimerSceance

urlpatterns = [
    path('ajoutfilm', ajoutFilm.as_view(), name="ajoutFilm"),
    path('ajoutsceance', ajoutsceance.as_view(), name="ajoutsceance"),
    path('ModifierSceance/<str:pk>/', ModifierSceance.as_view(), name="ModifierSceance"),
    path('SupprimerSceance/<str:pk>/', SupprimerSceance.as_view(), name="SupprimerSceance"),
    path('Modifierfilm/<str:pk>/', Modifierfilm.as_view(), name="Modifierfilm"),
    path('SupprimerFilm/<str:pk>/', SupprimerFilm.as_view(), name="SupprimerFilm"),
]