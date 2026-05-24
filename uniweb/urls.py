"""
URLs principales del proyecto uniweb.

Aquí se conectan todas las rutas del sistema:
  /           → home (vista principal con template)
  /saludo/    → primer endpoint de prueba (diapositiva 6)
  /estudiantes/registro/  → formulario para guardar un estudiante
  /estudiantes/           → lista de todos los estudiantes
  /productos/registro/    → formulario para guardar un producto
  /productos/             → lista de todos los productos
  /productos/editar/<id>/ → editar un producto por ID
  /productos/eliminar/<id>/ → eliminar un producto por ID
  /admin/     → panel de administración de Django
"""

from django.contrib import admin
from django.urls import path

# Importamos todas las vistas de la app estudiantes
from estudiantes.views import (
    saludo,                # primera vista de prueba (diapositiva 6)
    home,                  # vista principal con template (diapositiva 14)
    guardar_estudiante,    # guardar estudiante en BD (diapositiva 25)
    lista_estudiantes,     # listar estudiantes desde BD (diapositiva 26)
    registrar_producto,    # guardar producto en BD (diapositiva 33)
    lista_productos,       # listar productos (diapositiva 34)
    editar_producto,       # actualizar un producto (diapositiva 43)
    eliminar_producto,     # borrar un producto (diapositiva 44)
)

urlpatterns = [
    # Panel de administración de Django
    path("admin/", admin.site.urls),

    # Ruta raíz → renderiza home.html con contexto
    path("", home, name="home"),

    # Primer endpoint de prueba (Slide 6)
    path("saludo/", saludo, name="saludo"),

    # ─── Rutas de Estudiantes ───────────────────────────────────────────────
    # Formulario para registrar un nuevo estudiante (GET muestra form, POST guarda)
    path("estudiantes/registro/", guardar_estudiante, name="guardar_estudiante"),
    # Página que muestra todos los estudiantes guardados en la BD
    path("estudiantes/", lista_estudiantes, name="lista_estudiantes"),

    # ─── Rutas de Productos (CRUD completo) ────────────────────────────────
    # CREATE: mostrar formulario y guardar producto
    path("productos/registro/", registrar_producto, name="registrar_producto"),
    # READ: listar todos los productos
    path("productos/", lista_productos, name="lista_productos"),
    # UPDATE: editar un producto específico usando su ID
    path("productos/editar/<int:id>/", editar_producto, name="editar_producto"),
    # DELETE: eliminar un producto específico usando su ID
    path("productos/eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),
]
