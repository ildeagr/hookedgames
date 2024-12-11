const links = document.querySelectorAll('.menu a');
const formulario = document.querySelector('.formulario');

links.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const formId = link.dataset.form;
    // Aquí metemos la función para cargar el formulario correspondiente
    cargarFormulario(formId);
  });
});

function cargarFormulario(formId) {
  // Lógica para cargar el formulario según el ID
  // Puedes cargar el formulario desde un archivo HTML externo o generarlo dinámicamente
  if (formId === 'form1') {
    formulario.innerHTML = `
      <form action="ventas" method="post">
        <div class="campo">
          <label for="nombre">Id del juego:</label>
          <input type="text" id="nombre" name="Id">
        </div>
        <div class="campo">
          <label for="nombre">Sede:</label>
          <input type="text" id="nombre" name="Sede">
        </div>
        <div class="campo">
          <label for="nombre">Fecha:</label>
          <input type="text" id="nombre" name="Fecha">
        </div>
        <div class="campo">
          <label for="nombre">Id vendedor:</label>
          <input type="text" id="nombre" name="Vendedor">
        </div>
        <div class="campo">
          <button type="submit">Enviar</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form2') {
    formulario.innerHTML = `
      <form action="ventascomletas" method="post">
        <div class="campo_submit">
          <button type="submit">Tabla de ventas</button>
        </div>
      </form>
    `;
  }
  // ... otros formularios
}