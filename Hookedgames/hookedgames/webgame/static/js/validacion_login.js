document.getElementById('myform').addEventListener('submit', function(event){
  event.preventDefault();

  const contra = document.getElementById('contrasena').value;
  const email = document.getElementById('email').value;


   if (contra === "" || email === "") {
        alert('Por favor, rellene todos los campos.');
   }else {
        event.currentTarget.submit();
   }
  });