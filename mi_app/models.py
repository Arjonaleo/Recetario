from django.db import models

# Modelo para Categorías de recetas (ej: Postres, Sopas)
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)  # ID automático
    nombre = models.CharField(max_length=100)  # Nombre de la categoría, máx 100 caracteres

    def __str__(self):
        return self.nombre  # Muestra el nombre en el admin

    class Meta:
        verbose_name = "Categoría"  # Nombre singular en admin
        verbose_name_plural = "Categorías"  # Plural

# Modelo para Recetas
class Receta(models.Model):
    DIFICULTAD_CHOICES = [  # Opciones para dificultad
        ('facil', 'Fácil'),
        ('medio', 'Medio'),
        ('dificil', 'Difícil'),
    ]

    id = models.AutoField(primary_key=True)  # ID automático
    nombre = models.CharField(max_length=100)  # Nombre de la receta
    descripcion = models.TextField()  # Descripción detallada (texto largo)
    ingredientes = models.TextField()  # Lista de ingredientes (texto simple, ej: "Harina, huevos...")
    tiempo_preparacion = models.IntegerField()  # Tiempo en minutos
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES)  # Dificultad con opciones
    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha automática al crear
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación: una receta pertenece a una categoría

    def __str__(self):
        return self.nombre  # Muestra el nombre en el admin

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"