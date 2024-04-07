from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from salles.forms import AjoutSallesForm, ModifierSalleForm
from films.models import salles


def ajoutSalle(request):
    if request.method == "POST":
        form = AjoutSallesForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/salles")
    else:
        form = AjoutSallesForm()
    return render(request, "ajoutSalle.html", {'form':form})

def listeSalle(request):
    return render(request, "listeSalles.html", {'salles':salles.objects.all()})

def modifierSalle(request, pk):
    uneSalle = salles.objects.get(id=pk) 
    print(uneSalle)
    if request.method == "POST":
        form = ModifierSalleForm(request.POST, instance=uneSalle)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect("/salles/listeSalle/")
    else:
        form = ModifierSalleForm(instance=uneSalle)
    return render(request, 'modifierSalle.html', {'form': form})

def supprimerSalle(request, pk):
    salles.objects.get(id=pk).delete()
    return HttpResponseRedirect("/salles/listeSalle/")
