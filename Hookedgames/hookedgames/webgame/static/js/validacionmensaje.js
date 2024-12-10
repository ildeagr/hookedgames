const form = document.getElementById('myform');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const nombre = document.getElementById('nombre').value;
  const email = document.getElementById('email').value;
  const telefono = document.getElementById('telefono').value;
  const textarea = document.getElementById('mimensage');

  const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const regexTelefono = /^[0-9]{9}$/;

   if (nombre === "") {
        alert('Por favor, ingresa un nombre válido.');
        return false;
    }

    else if (!regexTelefono.test(telefono) || telefono === "") {
        alert('Por favor, ingresa un número de teléfono válido.');
        return false;
    }

    else if (!regexEmail.test(email) || email === "") {
        alert('Por favor, ingresa un correo electrónico válido.');
        return false;
    }

    else if (textarea.value.length > textarea.maxLength || textarea === "") {
        alert('Has excedido el límite de caracteres o el mensaje está vacio.');
        textarea.value = textarea.value.slice(0, textarea.maxLength); // Cortar el texto extra
        return false;
    }

    form.submit();
  });