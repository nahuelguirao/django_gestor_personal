from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TareaForm
from .models import Tarea

# Create Tarea
@login_required
def crear(request):
    if request.method == 'GET':
        return render(request, 'paginas/nueva_tarea.html', {
        'form' : TareaForm
        })
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user
            tarea.save()
            return redirect('leer')
        else:
            return render(request, 'paginas/nueva_tarea.html', {
            'form' : TareaForm
            })

# Read Tarea
@login_required
def leer(request):
    usuario = request.user
    tareas = Tarea.objects.filter(user=usuario)
    return render(request, 'paginas/mis_tareas.html', {
        'tareas' : tareas,
        'usuario' : usuario,
    })