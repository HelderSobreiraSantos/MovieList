from django.shortcuts import render, redirect
from .forms import FilmeForm
from .models import Filme, Genero
from .forms import GeneroForm

def addFilme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmeForm()
    return render(request, 'addfilme.html', {'form': form})

def deleteFilme(request, pk):
    filme = Filme.objects.get(id=pk)
    filme.delete()
    return redirect('index')

def updateFilme(request, id):
    filme = Filme.objects.get(id=id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'updatefilme.html', {'form': form})

def index(request):
    filmes = Filme.objects.all()
    return render(request, 'index.html', {'filmes': filmes})

def addGenero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GeneroForm()
    return render(request, 'addgenero.html', {'form': form})
