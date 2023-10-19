const boton = document.getElementById('img-menu')

const estructuraNavbar = document.getElementById('navbar')

const navbar = document.getElementById('menu')


boton.addEventListener('click', function() {
    navbar.classList.toggle('activo');
    estructuraNavbar.classList.toggle('activo');
})
