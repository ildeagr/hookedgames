const boton = document.getElementById('button_add');
const cantidad = document.getElementById('cantidad');

boton.addEventListener('click', () => {
  const inputcantidad =  parseInt(cantidad.value);
  cantidad.textContent = inputcantidad + 1;;
  inputcantidad = cantidadEnCarrito;
  // Aquí puedes agregar la lógica para actualizar el carrito en tu backend o almacenamiento local si lo deseas
});