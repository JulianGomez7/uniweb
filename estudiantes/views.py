"""
views.py — Capa de lógica (Vistas / Controladores)

En Django, las "views" son funciones (o clases) que:
  1. Reciben una petición HTTP (request)
  2. Procesan la lógica necesaria
  3. Devuelven una respuesta HTTP (HTML, JSON, redirección, etc.)

Flujo general (diapositiva 10 y 16):
  URL → View (Python) → Template (HTML) → Response al navegador

Concepto ORM (diapositiva 25):
  La capa View actúa como intermediaria entre el template y los modelos (BD).
  Nunca pongas lógica de negocio directamente en el HTML ni en la BD.
"""

from django.http import HttpResponse          # respuesta simple de texto
from django.shortcuts import render, redirect  # renderizar templates y redirigir
from django.db import transaction              # para transacciones atómicas (diapositiva 50)

from .models import Estudiante, Producto       # importamos nuestros modelos ORM


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 1: saludo — primer endpoint de prueba
# Diapositiva 6: primer endpoint funcional del proyecto
# URL: /saludo/
# ─────────────────────────────────────────────────────────────────────────────
def saludo(request):
    """
    Vista más simple posible: devuelve texto plano directamente.
    No usa template ni base de datos.
    """
    return HttpResponse("Hola desde el servidor (Django)")


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 2: home — página principal con template
# Diapositivas 12-15: usar render() para pasar contexto al template
# URL: /
# ─────────────────────────────────────────────────────────────────────────────
def home(request):
    """
    Vista principal. Renderiza home.html y le pasa un diccionario de contexto.
    render() hace tres cosas:
      - Carga el template indicado
      - Le inyecta las variables del contexto
      - Devuelve el HTML resultante como HttpResponse
    """
    # Contexto: datos que el template puede usar con {{ variable }}
    contexto = {
        "titulo": "Home Estudiantes"
    }
    # render(request, 'ruta/del/template.html', contexto)
    return render(request, "estudiantes/home.html", contexto)


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 3: guardar_estudiante — CREATE de estudiantes
# Diapositiva 25: usar el ORM para guardar en BD
# URL: /estudiantes/registro/
# ─────────────────────────────────────────────────────────────────────────────
def guardar_estudiante(request):
    """
    Maneja dos métodos HTTP:
      GET  → muestra el formulario vacío (registro_estudiante.html)
      POST → toma los datos del form, los guarda en BD, redirige a la lista
    """
    if request.method == "POST":
        # Obtener los datos enviados en el formulario
        nombre = request.POST.get("nombre")
        edad = int(request.POST.get("edad"))  # convertir a entero

        # ORM: crear un nuevo registro en la tabla Estudiante
        # Equivale a: INSERT INTO estudiantes_estudiante (nombre, edad) VALUES (...)
        Estudiante.objects.create(nombre=nombre, edad=edad)

        # Después de guardar, redirigir a la lista (evita reenvío del form con F5)
        return redirect("lista_estudiantes")

    # Si es GET, simplemente mostrar el formulario vacío
    return render(request, "estudiantes/registro_estudiante.html")


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 4: lista_estudiantes — READ de estudiantes
# Diapositiva 26: listar todos los registros de la BD
# URL: /estudiantes/
# ─────────────────────────────────────────────────────────────────────────────
def lista_estudiantes(request):
    """
    Consulta todos los estudiantes guardados en la BD y los manda al template.
    ORM: .objects.all() → SELECT * FROM estudiantes_estudiante
    """
    # Traer todos los estudiantes de la base de datos
    estudiantes = Estudiante.objects.all()

    # Pasar la lista al template como variable de contexto
    return render(request, "estudiantes/lista_estudiantes.html", {
        "estudiantes": estudiantes
    })


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 5: registrar_producto — CREATE de productos
# Diapositiva 33: misma lógica que estudiante pero con Producto
# URL: /productos/registro/
# ─────────────────────────────────────────────────────────────────────────────
def registrar_producto(request):
    """
    GET  → muestra formulario de registro de producto
    POST → guarda el producto en BD y redirige a la lista
    """
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")  # DecimalField acepta string desde el form

        # ORM: insertar nuevo producto en la tabla
        Producto.objects.create(nombre=nombre, precio=precio)

        return redirect("lista_productos")

    return render(request, "estudiantes/registro_producto.html")


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 6: lista_productos — READ de productos
# Diapositiva 34: listar todos los productos
# URL: /productos/
# ─────────────────────────────────────────────────────────────────────────────
def lista_productos(request):
    """
    Trae todos los productos de la BD y los renderiza en el template de lista.
    """
    productos = Producto.objects.all()

    return render(request, "estudiantes/lista_productos.html", {
        "productos": productos
    })


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 7: editar_producto — UPDATE de productos
# Diapositiva 43: actualizar un producto por su ID
# URL: /productos/editar/<id>/
# ─────────────────────────────────────────────────────────────────────────────
def editar_producto(request, id):
    """
    Busca el producto por su ID, luego:
      GET  → muestra formulario con los datos actuales del producto
      POST → guarda los cambios en la BD y redirige a la lista

    El parámetro 'id' viene de la URL: /productos/editar/3/ → id = 3
    """
    # ORM: buscar un registro específico por su ID (clave primaria)
    # Equivale a: SELECT * FROM ... WHERE id = <id>
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        # Actualizar los campos del objeto con los nuevos valores del form
        producto.nombre = request.POST.get("nombre")
        producto.precio = request.POST.get("precio")

        # ORM: guardar los cambios → UPDATE en la BD
        producto.save()

        return redirect("lista_productos")

    # GET: mostrar el formulario prellenado con los datos del producto
    return render(request, "estudiantes/editar_producto.html", {
        "producto": producto
    })


# ─────────────────────────────────────────────────────────────────────────────
# VISTA 8: eliminar_producto — DELETE de productos
# Diapositiva 44: eliminar un producto por su ID
# URL: /productos/eliminar/<id>/
# ─────────────────────────────────────────────────────────────────────────────
def eliminar_producto(request, id):
    """
    Busca el producto por ID y lo borra de la BD.
    Luego redirige a la lista.
    ORM: .delete() → DELETE FROM ... WHERE id = <id>
    """
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect("lista_productos")


# ─────────────────────────────────────────────────────────────────────────────
# EJEMPLO EXTRA: transacción atómica
# Diapositiva 50: @transaction.atomic garantiza que si algo falla, TODO se revierte
# ─────────────────────────────────────────────────────────────────────────────
@transaction.atomic
def registrar_compra_ejemplo(request):
    """
    Ejemplo de transacción atómica.
    Si cualquier línea dentro del bloque falla, se revierten TODOS los cambios.
    Útil para operaciones que deben ocurrir juntas (factura + detalle, etc.)

    NOTA: Esta vista no está conectada a ninguna URL en este proyecto,
          es solo un ejemplo didáctico de cómo se usa @transaction.atomic.
    """
    # Ambas operaciones ocurren juntas o ninguna ocurre
    producto = Producto.objects.create(
        nombre="Mouse",
        precio=100
    )
    # Si hubiera un modelo Movimiento, se crearía aquí también
    # Movimiento.objects.create(descripcion="Compra realizada")

    return redirect("lista_productos")
