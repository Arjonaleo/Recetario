from django.contrib import admin
from .models import Usuario, Vehiculo


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_nacimiento")
    search_fields = ("nombre", )
    list_filter = ("fecha_nacimiento", )


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_compra", "usuario")