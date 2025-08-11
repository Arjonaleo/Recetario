document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const filterForm = document.getElementById('filter-form');
    const recetasList = document.getElementById('recetas-list').querySelector('ul');

    // Función para cargar recetas con fetch
    function loadRecetas(busqueda = '', dificultad = '') {
        let url = '/recetas/?';
        if (busqueda) url += `busqueda=${busqueda}&`;
        if (dificultad) url += `dificultad=${dificultad}`;
        fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
            .then(response => response.json())
            .then(data => {
                recetasList.innerHTML = '';
                if (data.length === 0) {
                    recetasList.innerHTML = '<li>No hay recetas.</li>';
                } else {
                    data.forEach(receta => {
                        const li = document.createElement('li');
                        li.innerHTML = `<a href="/recetas/${receta.id}/">${receta.nombre}</a> - Dificultad: ${receta.dificultad} - Tiempo: ${receta.tiempo_preparacion} min`;
                        recetasList.appendChild(li);
                    });
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Evento submit para búsqueda
    searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const busqueda = document.getElementById('busqueda').value;
        loadRecetas(busqueda, document.getElementById('dificultad').value);
    });

    // Evento submit para filtro
    filterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const dificultad = document.getElementById('dificultad').value;
        loadRecetas(document.getElementById('busqueda').value, dificultad);
    });

    // Carga inicial
    loadRecetas();
});