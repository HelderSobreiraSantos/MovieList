from django.shortcuts import render, redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from .forms import FilmeForm, UsuarioForm
from django.contrib.auth.hashers import make_password, check_password
from .models import Filme, Genero, Usuario
from .forms import GeneroForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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
            return render(request, 'paginaDoUsuario.html', context) #,context  
        else:
            error_message = "Usuário Ou Senha Incorretos."

    return render(request, 'logar.html', {'error_message': error_message})

def sair(request):
    logout(request)  # Faz o logout do usuário
    return redirect('index')

def paginaDoUsuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'paginaDoUsuario.html', {'usuario': usuario})



