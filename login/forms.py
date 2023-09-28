from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Creo un formulario de registro que hereda las propiedades del formulario de creacion de usuarios Django
class RegistroForm(UserCreationForm):
    #Input Nombre
    first_name = forms.CharField(
        label= 'Nombre',
        widget= forms.TextInput(attrs={'placeholder':'Nombre...'}),
    )
    #Input Apellido
    last_name = forms.CharField(
        label='Apellido',
        widget= forms.TextInput(attrs={'placeholder':'Apellido...'}),
    )
    #Input username
    username = forms.CharField(
        label='Username',
        widget= forms.TextInput(attrs={'placeholder':'Username...'})
    )
    #Input email
    email = forms.EmailField(
        label='Email',
        widget= forms.EmailInput(attrs={'placeholder': 'Email...'})
    )
    #Input contraseña
    password1 = forms.CharField(
        label = 'Contraseña',
        widget= forms.PasswordInput(attrs={'placeholder':'Contraseña...'})
    )
    #Input repetir contraseña
    password2 = forms.CharField(
        label= 'Repita Contraseña',
        widget= forms.PasswordInput(attrs={'placeholder':'Repita contraseña...'})
    )
    
    #Modelo a utilizar (Predeterminado User de Django)
    class Meta:
        model = User 
        fields = ['first_name','last_name','username','email','password1','password2']
        

class IncioSesionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Ingrese su contraseña'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),)
    
    class Meta:
        model = User
        fields = ['email','password']