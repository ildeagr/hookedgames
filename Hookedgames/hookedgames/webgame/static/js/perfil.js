function habilitarInput() {
  document.getElementById("form_user").disabled = false;
  document.getElementById("form_nombre").disabled = false;
  document.getElementById("form_dni").disabled = false;
  document.getElementById("form_email").disabled = false;
  document.getElementById("form_telf").disabled = false;

  document.getElementById("form_submit").style.display = "block";
  document.getElementById("form_modificar").style.display = "none";
}