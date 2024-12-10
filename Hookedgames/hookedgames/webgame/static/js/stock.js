const links = document.querySelectorAll('.menu a');
const formulario = document.querySelector('.formulario');

formulario.innerHTML = `
      <form action="stockcompleto" method="post">
        <div class="campo_submit">
          <button type="submit">Ver stock completo</button>
        </div>
      </form>
    `;

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
      <form action="buscarstock" method="post">
        <div class="campo">
          <label for="nombre">Id del juego:</label>
          <input type="text" id="nombre" name="nombre">
        </div>
        <div class="campo">
          <button type="submit">Enviar</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form2') {
    formulario.innerHTML = `
      <form action="modificarstock" method="post">
        <div class="campo">
          <label for="nombre">Id del juego:</label>
          <input type="text" id="nombre" name="nombre">
        </div>
        <div class="campo">
          <label for="nombre">Indicar cantidad en stock:</label>
          <input type="text" id="nombre" name="nombre">
        </div>
        <div class="campo">
          <button type="submit">Enviar</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form3') {
    formulario.innerHTML = `
      <form action="stockcompleto" method="post">
        <div class="campo_submit">
          <button type="submit">Ver stock completo</button>
        </div>
      </form>
    `;
  }
  // ... otros formularios
}