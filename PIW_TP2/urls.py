from django.contrib import admin
from django.urls import path, include
from PIW_TP2.views import *
from usagers.views import enregistrement
from django.contrib.auth import views as authentification_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilView),
    path('apropos/', aProposView),
    path('films/', include("films.urls")),
    path('salles/', include("salles.urls")),
    path('administrateur/', include("administrateur.urls")),
    path('enregistrement/',enregistrement, name='enregistrement'),
    path('login/', authentification_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authentification_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
]
