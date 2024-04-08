from django.urls import path
from films.views import afficheFilm, detailFilm, detailSceance, reserverSceance


urlpatterns = [
    path('affiche', afficheFilm, name="afficheFilm"),
    path('detail/<str:pk>/', detailFilm, name="detailFilm"),
    path('detailsceance/<str:pk>/', detailSceance, name="detailSceance"),
    path('reserversceance/<str:pk>/', reserverSceance, name="reserverSceance"),
]
