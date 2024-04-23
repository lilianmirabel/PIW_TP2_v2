from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import enregistrementForm
# Create your views here.

def enregistrement(request):
  if request.method == 'POST':
    form = enregistrementForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Bonjour {username} vous êtes enregistre')
      return redirect('login')
  else:
    form = enregistrementForm()
  return render(request, 'enregistrement.html', {'form': form})
