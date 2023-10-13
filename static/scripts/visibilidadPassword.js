// CAMBIA EL TIPO DE INPUT AL CLICKEAR EL CHECKBOX 

document.addEventListener("DOMContentLoaded", function() {
    const checkbox = document.getElementById('input-mostrar-contraseña');
    const inputContrasena = document.getElementById('id_password');

    checkbox.addEventListener('change', function(){
        if (checkbox.checked){
            inputContrasena.type = 'text';
        } else {
            inputContrasena.type = 'password';
        }
    })
})