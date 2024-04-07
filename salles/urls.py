from django.urls import path
from salles.views import *


urlpatterns = [
    path('ajoutSalle/', ajoutSalle, name="ajoutSalle"),
    path('listeSalle/', listeSalle, name="listeSalle"),
    path('modifierSalle/<str:pk>/', modifierSalle, name="modifierSalle"),
    path('supprimerSalle/<str:pk>/', supprimerSalle, name="supprimerSalle"),
    path('', ajoutSalle),
]
