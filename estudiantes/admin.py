"""
admin.py — Panel de Administración de Django

Registrar los modelos aquí permite gestionarlos desde:
  http://127.0.0.1:8000/admin/

Para crear un superusuario:
  python manage.py createsuperuser
"""

from django.contrib import admin
from .models import Estudiante, Producto

# Registrar Estudiante en el panel admin
admin.site.register(Estudiante)

# Registrar Producto en el panel admin
admin.site.register(Producto)
