from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaTarefa, name='lista-tarefa'),
    path('novaTarefa/', views.novaTarefa, name='nova-tarefa')
 
]
