"""
models.py — Capa de datos (ORM)

Concepto clave (diapositivas 18-22):
  Tablas → Clases
  Filas   → Objetos

Cada clase que hereda de models.Model se convierte en una tabla en la BD.
Cada atributo de la clase se convierte en una columna de esa tabla.
Django genera el SQL necesario automáticamente con las migraciones.
"""

from django.db import models


# ─── MODELO ESTUDIANTE ───────────────────────────────────────────────────────
# Paso 2 del ORM (diapositiva 23): crear primera tabla
# Esto genera la tabla: estudiantes_estudiante en SQLite
class Estudiante(models.Model):
    # CharField = columna de texto con longitud máxima
    nombre = models.CharField(max_length=100)
    # IntegerField = columna de número entero
    edad = models.IntegerField()

    def __str__(self):
        # Representación legible del objeto (se usa en el admin y en prints)
        return self.nombre

    class Meta:
        # Nombre de la tabla en español para el admin de Django
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


# ─── MODELO PRODUCTO ─────────────────────────────────────────────────────────
# Actividad en clase (diapositiva 31-32): aplicar la misma lógica con Producto
# Esto genera la tabla: estudiantes_producto en SQLite
class Producto(models.Model):
    # CharField = nombre del producto (texto)
    nombre = models.CharField(max_length=100)
    # DecimalField = precio con decimales (ej: 9999.99)
    #   max_digits    → dígitos totales permitidos
    #   decimal_places → cuántos decimales se guardan
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Muestra el nombre cuando se imprime el objeto
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
