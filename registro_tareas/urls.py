from django.urls import path
from . import views

urlpatterns = [
    path('crear/tarea', views.crear, name='crear'),
    path('mis/tareas', views.leer, name='leer'),
    path('editar/tarea/<int:id>', views.actualizar, name='actualizar'),
    path('eliminar/tarea/<int:id>', views.eliminar, name='eliminar')
]

