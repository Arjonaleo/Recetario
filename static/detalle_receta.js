document.addEventListener('DOMContentLoaded', () => {
    // Ejemplo: Evento click en volver (opcional, ya que es link simple)
    const volverLink = document.querySelector('footer a');
    volverLink.addEventListener('click', (e) => {
        console.log('Volviendo a la lista');  // Para demo; puedes agregar más
    });
});