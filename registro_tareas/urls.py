from django.urls import path
from . import views

urlpatterns = [
    path('crear/tarea', views.crear, name='crear'),
    path('mis/tareas', views.leer, name='leer')
]

