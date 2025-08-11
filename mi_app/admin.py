from django.contrib import admin
from .models import Categoria, Receta

# Registro para Categoría
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)  # Muestra nombre en lista
    search_fields = ("nombre",)  # Busca por nombre

# Registro para Receta
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "dificultad", "tiempo_preparacion", "categoria")  # Columnas en lista
    search_fields = ("nombre", "descripcion")  # Busca por nombre o descripción
    list_filter = ("dificultad", "categoria")  # Filtros por dificultad y categoría