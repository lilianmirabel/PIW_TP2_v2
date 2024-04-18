from django.urls import path
from films.views import afficheFilm, detailFilm, DetailSeance, reserverSceance


urlpatterns = [
    path('affiche', afficheFilm.as_view(), name="afficheFilm"),
    path('detail/<str:pk>/', detailFilm.as_view(), name="detailFilm"),
    path('detailsceance/<str:pk>/', DetailSeance.as_view(), name="detailSceance"),
    path('reserversceance/<str:pk>/', reserverSceance.as_view(), name="reserverSceance"),
]
