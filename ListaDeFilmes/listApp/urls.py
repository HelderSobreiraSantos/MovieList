from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('genero/', views.verGenero, name='verGenero'),
path('addFilme/', views.addFilme, name='addFilme'),
path('deleteFilme/<str:pk>/', views.deleteFilme, name='deleteFilme'),
path('deleteGenero/<str:pk>/', views.deleteGenero, name='deleteGenero'),
]