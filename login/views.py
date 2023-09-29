from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

#Formularios de Registro e Inicio de sesion
from .forms import RegistroForm, IncioSesionForm

# Vista de inicio
def index(request):
    return render(request, 'paginas/inicio.html')

# Vista de registro de nuevo usuario
def registro(request):
    if request.method == 'GET':
        return render(request, 'paginas/registro.html',{
            'form' : RegistroForm
        })
    if request.method == 'POST':
        nuevo_usario = RegistroForm(request.POST)
        #Si los datos ingresados son correctos guarda el nuevo usuario y redirecciona
        if nuevo_usario.is_valid():
            nuevo_usario.save()
            return redirect('index')
        else:
            return render(request, 'paginas/registro.html', {
                'form' : RegistroForm
            })

# Vista de inicio de sesión
def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request,'paginas/inicio_sesion.html', {
            'form' : IncioSesionForm
        })
    if request.method == 'POST':
        email_usuario = request.POST['email']
        contraseña_usuario = request.POST['password']
        #Busca un usuario asociado con el email ingresado 
        usuario = User.objects.filter(email=email_usuario).first()
        #Si lo encuentra verifica si la contraseña es la correspondiente
        if usuario is not None and usuario.check_password(contraseña_usuario):
            #Genera una sesion nueva
            login(request, usuario)
            return redirect('index')
        #Devuelve el inicio de sesión informando credenciales incorrectas
        else:
            return render(request,'paginas/inicio_sesion.html',{
                'form' : IncioSesionForm,
                'error' : 'Credenciales incorrectas.'
            })

# Vista para cerrar sesión
@login_required
def cerrar_sesion(request):
    #Cierra la sesión
    logout(request)
    return redirect('index')