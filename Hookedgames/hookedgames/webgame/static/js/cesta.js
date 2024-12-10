function sumarproducto() {
    // Obtener el elemento span de la cantidad
    const cantidad = document.querySelector("#cantidad");
    const valorActual =  parseInt(cantidad.textContent);

    const nuevoValor = valorActual + 1;
    cantidad.textContent = nuevoValor;
}

function restarproducto() {
    // Obtener el elemento span de la cantidad
    const cantidad = document.querySelector("#cantidad");
    const valorActual =  parseInt(cantidad.textContent);

    if(valorActual > 1){
        const nuevoValor = valorActual - 1;
        cantidad.textContent = nuevoValor;
    }
}
