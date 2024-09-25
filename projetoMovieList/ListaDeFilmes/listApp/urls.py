from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addFilme/', views.addFilme, name='addFilme'),
    path('deleteFilme/<str:pk>/', views.deleteFilme, name='deleteFilme'),
    path('updateFilme/<int:id>/', views.updateFilme, name='updateFilme'),
    path('addGenero/', views.addGenero, name='addGenero'),
    path('addUsuario/', views.addUsuario, name='addUsuario'),
    path('paginaDoUsuario/', views.paginaDoUsuario, name='paginaDoUsuario'), #<int:usuario_id>/
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name='sair'),
    path('addListaDeFilmes/', views.addListaDeFilmes, name='addListaDeFilmes'),
]
