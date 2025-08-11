from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Receta, Categoria

# Vista para lista de recetas (todas, con búsqueda y filtro)
class ListaRecetasView(View):
    def get(self, request):
        recetas = Receta.objects.all()  # Obtiene todas las recetas
        
        # Búsqueda por nombre (barra de búsqueda)
        busqueda = request.GET.get('busqueda')
        if busqueda:
            recetas = recetas.filter(nombre__icontains=busqueda)  # Busca sin importar mayúsculas
        
        # Filtro por dificultad (ej: ?dificultad=facil)
        dificultad = request.GET.get('dificultad')
        if dificultad:
            recetas = recetas.filter(dificultad=dificultad)
        
        # Si es una petición AJAX, devuelve JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = list(recetas.values('id', 'nombre', 'dificultad', 'tiempo_preparacion'))
            return JsonResponse(data, safe=False)
        
        # Para peticiones normales, renderiza el template
        context = {
            'recetas': recetas,
            'dificultades': Receta.DIFICULTAD_CHOICES,  # Para mostrar opciones de filtro
        }
        return render(request, 'lista_recetas.html', context)

# Vista para detalle de una receta individual
class DetalleRecetaView(View):
    def get(self, request, id):
        receta = get_object_or_404(Receta, id=id)  # Obtiene la receta o error 404 si no existe
        context = {'receta': receta}
        return render(request, 'detalle_receta.html', context)
    