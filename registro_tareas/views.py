from django.shortcuts import render, redirect, get_object_or_404
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

# Update Tarea
@login_required
def actualizar(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('leer')
        else:
            form = TareaForm(instance=tarea)
    else:
        form = TareaForm(instance=tarea)
    
    return render(request,'paginas/editar_tarea.html', {
        'tarea' : tarea,
        'form' : form,
    })