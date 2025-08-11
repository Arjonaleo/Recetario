from django.contrib import admin
from django.urls import path
from mi_app.views import ListaRecetasView, DetalleRecetaView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', ListaRecetasView.as_view(), name='home'),
    path('recetas/', ListaRecetasView.as_view(), name='lista_recetas'),  # Lista de recetas
    path('recetas/<int:id>/', DetalleRecetaView.as_view(), name='detalle_receta'),  # Detalle por ID
]