const links = document.querySelectorAll('.menu a');
const formulario = document.querySelector('.formulario');

formulario.innerHTML = `
      <form action="buscarstock" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="Id">
        </div>
        <div class="campo">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="Nombre">
        </div>
        <div class="campo">
          <label for="nombre">Correo:</label>
          <input type="text" id="nombre" name="Correo">
        </div>
        <div class="campo">
          <label for="nombre">Teléfono:</label>
          <input type="text" id="nombre" name="Telefono">
        </div>
        <div class="campo">
          <label for="nombre">Sede:</label>
          <input type="text" id="nombre" name="Sede">
        </div>
        <div class="campo">
          <button type="submit">Dar alta</button>
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
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="Id">
        </div>
        <div class="campo">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="Nombre">
        </div>
        <div class="campo">
          <label for="nombre">Correo:</label>
          <input type="text" id="nombre" name="Correo">
        </div>
        <div class="campo">
          <label for="nombre">Teléfono:</label>
          <input type="text" id="nombre" name="Telefono">
        </div>
        <div class="campo">
          <label for="nombre">Sede:</label>
          <input type="text" id="nombre" name="Sede">
        </div>
        <div class="campo">
          <button type="submit">Dar alta</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form2') {
    formulario.innerHTML = `
      <form action="modificarstock" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="Id">
        </div>
        <div class="campo">
          <button type="submit">Dar baja</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form3') {
    formulario.innerHTML = `
      <form action="modificarstock" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="Id">
        </div>
        <div class="campo">
          <button type="submit">Modificar</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form4') {
    formulario.innerHTML = `
      <form action="modificarstock" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="Id">
        </div>
        <div class="campo">
          <button type="submit">Consultar</button>
        </div>
      </form>
    `;
  }
  // ... otros formularios
}