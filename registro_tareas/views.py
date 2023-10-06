from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TareaForm

# Create your views here.
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
            return redirect('index')
        else:
            return render(request, 'paginas/nueva_tarea.html', {
            'form' : TareaForm
            })