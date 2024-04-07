from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def accueilView(request):
    return HttpResponseRedirect("/films/affiche#")
    
def aProposView(request):
    return render(request, 'apropos.html')