from django.shortcuts import render, redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from .forms import FilmeForm, UsuarioForm
from django.contrib.auth.hashers import make_password, check_password
from .models import Filme, Genero, Usuario, ListaDeFilmes
from .forms import GeneroForm

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


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
    listas_de_filmes = ListaDeFilmes.objects.all()  # Obter todas as listas de filmes
    return render(request, 'index.html', {'filmes': filmes, 'listas_de_filmes': listas_de_filmes})

def addGenero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addGenero')
    else:
        form = GeneroForm()
    return render(request, 'addgenero.html', {'form': form})

def addUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(usuario.senha)  # Criptografando a senha
            usuario.save()
            return redirect('paginaDoUsuario', usuario_id=usuario.id)  # Redireciona para a página do usuário
    else:
        form = UsuarioForm()
    return render(request, 'addUsuario.html', {'form': form})

def logar(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        print(f"Tentando autenticar: {email}")
        user = Usuario.objects.get(email=email)
        username = user.nome
        usuario = authenticate(request, username=username, password=senha)

        if usuario is not None:
            login(request, usuario)
            context = {
                'usuario': usuario,
            }
            return redirect('http://127.0.0.1:8000/')
            #return redirect(request, 'index.html') #lembrar de retirar o context e fazer tudo no html  
        else:
            error_message = "Usuário Ou Senha Incorretos."

    return render(request, 'logar.html', {'error_message': error_message})

def sair(request):
    logout(request)
    return redirect('index')

@login_required(login_url="logar")
def paginaDoUsuario(request):
    usuario_atual = Usuario.objects.get(nome=request.user.username)
    filmes = Filme.objects.all()
    context = {
        'filmes':filmes,
    }
    return render(request, 'paginaDoUsuario.html', context)

@login_required(login_url="logar")
def addListaDeFilmes(request):
    usuario_atual = Usuario.objects.get(nome=request.user.username)

    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        filme_ids = request.POST.get('filmes').split(' ')
        genero=Genero.objects.get(id=1)
        filme1 = Filme.objects.get(id = filme_ids[0])
        #print("filmes entrando: ", filme_ids)
        lista_de_filmes = ListaDeFilmes(nome=nome, descricao=descricao, genero=genero, usuario=usuario_atual) #filmes=filme1
        lista_de_filmes.save()
        #print(f"Dados recebidos - Nome: {nome}, Descrição: {descricao}, IDs dos filmes: {filme_ids}")

        lista = ListaDeFilmes.objects.get(nome=nome)
        #for cont in range(len(filme_ids)):
        #    if filme_ids[cont] != " ":  
        #        lista.filmes.add(filme_ids[cont])
        #        print("numero de vezes:", cont)

        #print("numero de vezes:", filme_ids[0])
        lista.filmes.add(int(filme_ids[0]))
        #print("numero de vezes:", filme_ids[1])
        lista.filmes.add(int(filme_ids[1]))
        #print("numero de vezes:", filme_ids[2])
        lista.filmes.add(int(filme_ids[2]))
        #print("numero de vezes:", filme_ids[3])
        lista.filmes.add(int(filme_ids[3]))
        #print("numero de vezes:", filme_ids[4])
        lista.filmes.add(int(filme_ids[4]))
        #print("numero de vezes:", filme_ids[5])
        lista.filmes.add(int(filme_ids[5]))
        #print("numero de vezes:", filme_ids[6])
        lista.filmes.add(int(filme_ids[6]))

        return render(request, 'paginaDoUsuario.html')

#TypeError at /addListaDeFilmes/
#'ListaDeFilmes' object is not iterable
#Request Method:	POST
#Request URL:	http://127.0.0.1:8000/addListaDeFilmes/
#Django Version:	5.0.2
#Exception Type:	TypeError
#Exception Value:	
#'ListaDeFilmes' object is not iterable
#Exception Location:	C:\Users\filho\OneDrive\Documentos\GitHub\MovieList\projetoMovieList\envConfig\Lib\site-packages\django\template\defaulttags.py, line 197, in render
#Raised during:	listApp.views.addListaDeFilmes
#Python Executable:	C:\Users\filho\OneDrive\Documentos\GitHub\MovieList\projetoMovieList\envConfig\Scripts\python.exe
#Python Version:	3.12.2
#Python Path:	
#['C:\\Users\\filho\\OneDrive\\Documentos\\GitHub\\MovieList\\projetoMovieList\\ListaDeFilmes',
# 'C:\\Users\\filho\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
# 'C:\\Users\\filho\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
# 'C:\\Users\\filho\\AppData\\Local\\Programs\\Python\\Python312\\Lib',
# 'C:\\Users\\filho\\AppData\\Local\\Programs\\Python\\Python312',
# 'C:\\Users\\filho\\OneDrive\\Documentos\\GitHub\\MovieList\\projetoMovieList\\envConfig',
# 'C:\\Users\\filho\\OneDrive\\Documentos\\GitHub\\MovieList\\projetoMovieList\\envConfig\\Lib\\site-packages']
#Server time:	Tue, 24 Sep 2024 22:34:06 +0000