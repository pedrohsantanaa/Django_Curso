from django.shortcuts import render, redirect
from .models import Tarefas
from .forms import TarefaForm

# Create your views here.
def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})


def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        form.save()
        return redirect('/')
    
    else:
        form = TarefaForm()
        return render(request, 'tarefas/addTarefa.html', {'form':form})