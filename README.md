Catálogo de Recetas - Proyecto FullStack con Django
Descripción
Este proyecto es un sitio web FullStack desarrollado con el framework Django, diseñado como un catálogo de recetas (recetario de cocina). Permite a los usuarios gestionar y consultar recetas de cocina a través de una interfaz web. El backend utiliza una base de datos SQLite para almacenar recetas y categorías, gestionadas mediante el panel de administración de Django. El frontend renderiza vistas HTML con rutas definidas en Django, incluyendo una lista de recetas con búsqueda y filtros dinámicos (usando JavaScript y fetch), y una vista para detalles individuales. El diseño utiliza HTML semántico, estilos CSS separados, y lógica JavaScript para eventos y consumo de datos.
Funcionalidades Principales

Backend:
Base de datos SQLite con modelos Categoria y Receta.
Panel de administración para gestionar datos (agregar, editar, eliminar recetas/categorías).
Búsquedas básicas en la base de datos (por nombre, dificultad).


Frontend:
Lista de recetas con búsqueda por nombre y filtro por dificultad, implementados dinámicamente con JavaScript (fetch).
Vista de detalles para cada receta.
Estructura HTML semántica (<header>, <section>, <footer>).
Archivos CSS separados por cada HTML para estilos.
Archivos JavaScript separados para manejar eventos (submit, click) y peticiones fetch.


Tecnologías:
Django 5.2.5 para backend y rutas.
SQLite para la base de datos.
HTML5, CSS3, JavaScript para frontend.
Jazzmin para un panel de admin mejorado visualmente.



Requisitos
Para instalar y ejecutar este proyecto, necesitas lo siguiente:

Sistema operativo: Windows, macOS o Linux.
Python: Versión 3.13.5 o superior (descarga desde python.org).
Entorno virtual: Incluido con Python (venv).
Dependencias (se instalarán automáticamente):
Django==5.2.5
django-jazzmin==2.7.0
python-dotenv==1.0.1


Un navegador web moderno (Chrome, Firefox, etc.).
Opcional: Un editor de código como VS Code.

Instalación
Sigue estos pasos para instalar y configurar el proyecto en tu computadora. Todos los comandos se ejecutan en una terminal (PowerShell en Windows, Terminal en macOS/Linux).
1. Clona o Descarga el Proyecto

Si usas Git, clona el repositorio:git clone 
cd Recetario


O descarga el proyecto como ZIP y descomprímelo en una carpeta (ej: C:\Users\TuUsuario\Recetario).

2. Crea y Activa un Entorno Virtual
El entorno virtual aísla las dependencias del proyecto.

En Windows:
python -m venv venv
.\venv\Scripts\Activate.ps1


Si PowerShell da error ("running scripts is disabled"), abre PowerShell como administrador y ejecuta:Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Luego reintenta activar el entorno.


En macOS/Linux:
python3 -m venv venv
source venv/bin/activate


Verás (venv) en la terminal, indicando que el entorno está activo.


3. Instala las Dependencias
Con el entorno virtual activo, instala las librerías necesarias:
pip install django==5.2.5 django-jazzmin==2.7.0 python-dotenv==1.0.1

4. Aplica las Migraciones de la Base de Datos
Las migraciones crean las tablas en SQLite (db.sqlite3).
python manage.py makemigrations
python manage.py migrate

5. Crea un Superuser (Usuario Administrador)
Crea un usuario para acceder al panel de admin:
python manage.py createsuperuser


Ingresa un nombre de usuario (ej: admin), correo (opcional, puedes dejarlo en blanco), y una contraseña (ej: Recetario2025!).

6. (Opcional) Agrega Datos Iniciales

Ejecuta el servidor:python manage.py runserver


Ve a http://127.0.0.1:8000/admin/ en tu navegador.
Inicia sesión con tu superuser.
Agrega categorías (ej: "Postres", "Sopas") y recetas (ej: "Pastel de Chocolate", dificultad "Medio", tiempo 60 min).

Montaje y Ejecución
Para ejecutar el proyecto:

Asegúrate de estar en la carpeta Recetario con el entorno virtual activo ((venv)).
Ejecuta el servidor:python manage.py runserver


Abre un navegador y ve a:
http://127.0.0.1:8000/ (lista de recetas con búsqueda/filtro).
http://127.0.0.1:8000/recetas/<id>/ (detalles de una receta, ej: /recetas/1/).
http://127.0.0.1:8000/admin/ (panel de admin para gestionar datos).



Estructura del Proyecto
Recetario/
├── manage.py                # Script principal de Django
├── proyecto_3erparcial/     # Carpeta del proyecto
│   ├── __init__.py
│   ├── settings.py         # Configuración (BD, apps, static)
│   ├── urls.py             # Rutas principales (/recetas/, /admin/)
│   └── wsgi.py
├── mi_app/                  # App principal
│   ├── __init__.py
│   ├── admin.py            # Configuración del panel de admin
│   ├── models.py           # Modelos (Categoria, Receta)
│   ├── views.py            # Vistas (lista y detalles)
│   ├── templates/          # Templates HTML
│   │   ├── lista_recetas.html
│   │   └── detalle_receta.html
│   └── migrations/         # Migraciones de la BD
├── static/                  # Archivos estáticos
│   ├── lista_recetas.css
│   ├── detalle_receta.css
│   ├── lista_recetas.js
│   └── detalle_receta.js
├── db.sqlite3               # Base de datos SQLite
├── .env.dev                # Variables de entorno (SECRET_KEY, etc.)
└── README.md               # Esta documentación

Decisiones de Diseño

HTML Semántico: Uso de <header>, <section>, <footer> para accesibilidad y estructura clara, facilitando estilos CSS.
CSS Separado: Cada HTML tiene su propio CSS (lista_recetas.css, detalle_receta.css) para modularidad y evitar penalizaciones. Colores verdes para reflejar frescura (cocina).
JavaScript con Fetch: Búsqueda y filtro dinámicos en la lista de recetas usando fetch para consumir datos JSON desde Django, mejorando la experiencia sin recargas.
SQLite: Base de datos simple para cumplir el requisito de robustez básica, ideal para principiantes.
Jazzmin: Usado para un panel de admin más amigable visualmente, manteniendo simplicidad.
Eventos JS: Manejo de eventos submit/click para interactividad, cumpliendo requisitos sin complejidad innecesaria.

Solución de Problemas Comunes

Error "TemplateDoesNotExist": Verifica que los templates estén en mi_app/templates/ y que views.py los referencie correctamente (lista_recetas.html, no mi_app/lista_recetas.html).
Error "static tag invalid": Asegúrate de incluir {% load static %} al inicio de cada HTML.
Error de scripts en PowerShell: Ejecuta Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned como administrador.
Sin datos en la lista: Agrega recetas/categorías en /admin/.

Uso del Sitio

Lista de Recetas (/ o /recetas/): Muestra todas las recetas con búsqueda por nombre y filtro por dificultad (dinámicos via JS/fetch). Haz clic en una receta para ver detalles.
Detalles de Receta (/recetas/<id>/): Muestra información completa (nombre, descripción, ingredientes, tiempo, dificultad, categoría).
Admin (/admin/): Gestiona recetas y categorías con el superuser.

Autor

Leonarado Arjona Ramirez
