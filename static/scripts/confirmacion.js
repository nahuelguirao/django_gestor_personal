// Selecciona todos los botones de 'tarea completada'
document.querySelectorAll('.eliminar-tarea').forEach((botonEliminar) => {
    botonEliminar.addEventListener('click', function (event) {
      event.preventDefault();
      const tareaId = this.getAttribute('data-tarea-id');

      if (confirm('¿Seguro que deseas eliminar esta tarea?')) {
        window.location.href = this.getAttribute('href');
      }
    });
  });