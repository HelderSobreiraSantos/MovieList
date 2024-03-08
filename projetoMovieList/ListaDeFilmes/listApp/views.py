from django.shortcuts import redirect, render
from listApp.models import Filme
from django.http import HttpResponse

#from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello, world.")
    filmes = Filme.objects.all()
    context={'filmes':filmes}
    
    return render(request, 'index.html', context)
    #return render(request, 'index.html', context)

def addFilme(request):
    titulo = request.POST['filmTitulo']
    duracao = request.POST['filmDuracao']
    data = request.POST['filmData']

    filme = Filme(
        titulo = titulo,
        duracao = duracao,
        data = data,
    )
    filme.save()
    return redirect('http://127.0.0.1:8000/')

def deleteFilme(request, pk):
    filme = Filme.objects.get(id=pk)
    filme.delete()
    return redirect('http://127.0.0.1:8000/')