document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('myButton');
  const menu = document.getElementById('menu');

  button.addEventListener('click', () => {
    menu.classList.toggle('show');
  });
});