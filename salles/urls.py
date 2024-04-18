from django.urls import path
from salles.views import *

urlpatterns = [
    path('ajoutSalle/', ajoutSalle.as_view(), name="ajoutSalle"),
    path('listeSalle/', listeSalle.as_view(), name="listeSalle"),
    path('modifierSalle/<str:pk>/', modifierSalle.as_view(), name="modifierSalle"),
    path('supprimerSalle/<str:pk>/', supprimerSalle.as_view(), name="supprimerSalle"),
    path('', ajoutSalle.as_view()),  # Fix here
]
