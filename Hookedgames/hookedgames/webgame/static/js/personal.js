const links = document.querySelectorAll('.menu a');
const formulario = document.querySelector('.formulario');

formulario.innerHTML = `
      <form action="alta_empleado" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="id">
        </div>
        <div class="campo">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre">
        </div>
        <div class="campo">
          <label for="nombre">Password:</label>
          <input type="text" id="nombre" name="password">
        </div>
        <div class="campo">
          <label for="nombre">Puesto:</label>
          <input type="text" id="nombre" name="puesto">
        </div>
        <div class="campo">
          <label for="nombre">Sede:</label>
          <input type="text" id="nombre" name="sede">
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
      <form action="alta_empleado" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="id">
        </div>
        <div class="campo">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre">
        </div>
        <div class="campo">
          <label for="nombre">Password:</label>
          <input type="text" id="nombre" name="password">
        </div>
        <div class="campo">
          <label for="nombre">Puesto:</label>
          <input type="text" id="nombre" name="puesto">
        </div>
        <div class="campo">
          <label for="nombre">Sede:</label>
          <input type="text" id="nombre" name="sede">
        </div>
        <div class="campo">
          <button type="submit">Dar alta</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form2') {
    formulario.innerHTML = `
      <form action="modi_empleado" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="id">
        </div>
        <div class="campo">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre">
        </div>
        <div class="campo">
          <label for="nombre">Password:</label>
          <input type="text" id="nombre" name="password">
        </div>
        <div class="campo">
          <label for="nombre">Puesto:</label>
          <input type="text" id="nombre" name="puesto">
        </div>
        <div class="campo">
          <label for="nombre">Sede:</label>
          <input type="text" id="nombre" name="sede">
        </div>
        <div class="campo">
          <button type="submit">Modificar datos</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form3') {
    formulario.innerHTML = `
      <form action="baja_empleado" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="id">
        </div>
        <div class="campo">
          <button type="submit">Dar de baja</button>
        </div>
      </form>
    `;
  }

  else if (formId === 'form4') {
    formulario.innerHTML = `
      <form action="ver_empleado" method="post">
        <div class="campo">
          <label for="nombre">Id empleado:</label>
          <input type="text" id="nombre" name="id">
        </div>
        <div class="campo">
          <button type="submit">Mostrar empleado</button>
        </div>
      </form>
    `;
  }
  // ... otros formularios
}