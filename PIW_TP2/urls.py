from django.contrib import admin
from django.urls import path, include
from PIW_TP2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilView),
    path('apropos/', aProposView),
    path('films/', include("films.urls")),
    path('salles/', include("salles.urls")),
    path('administrateur/', include("administrateur.urls")),
]
