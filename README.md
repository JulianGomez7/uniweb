# 📚 Proyecto uniweb — Programación Integrada Web
### Andrés Alfonso Murgas Viloria

---

## ¿Qué hay en este proyecto?

Proyecto Django construido clase a clase siguiendo las diapositivas.
Cubre: servidor Django, vistas, templates, ORM, CRUD completo y transacciones.

---

## 🚀 Instalación y ejecución (desde cero)

### 1. Verificar Python
```bash
python --version
```

### 2. Entrar a la carpeta del proyecto
```bash
cd uniweb
```

### 3. Crear y activar entorno virtual
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac / Linux:
source venv/bin/activate
```

### 4. Instalar Django
```bash
pip install django
django-admin --version
```

### 5. Crear la base de datos (migraciones)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Correr el servidor
```bash
python manage.py runserver
```

---

## 🌐 URLs disponibles

| URL | Descripción |
|-----|-------------|
| http://127.0.0.1:8000/ | Página principal (home) |
| http://127.0.0.1:8000/saludo/ | Primer endpoint (Slide 6) |
| http://127.0.0.1:8000/estudiantes/registro/ | Registrar estudiante |
| http://127.0.0.1:8000/estudiantes/ | Listar estudiantes |
| http://127.0.0.1:8000/productos/registro/ | Registrar producto |
| http://127.0.0.1:8000/productos/ | Listar productos (con Editar/Eliminar) |
| http://127.0.0.1:8000/admin/ | Panel admin de Django |

---

## 📂 Estructura del proyecto

```
uniweb/
│
├── manage.py                  ← punto de entrada (runserver, migrate, etc.)
│
├── uniweb/                    ← configuración global del proyecto
│   ├── settings.py            ← BD, apps instaladas, templates
│   └── urls.py                ← rutas principales
│
├── estudiantes/               ← app modular
│   ├── models.py              ← ORM: Estudiante y Producto (tablas en BD)
│   ├── views.py               ← lógica: saludo, home, CRUD estudiantes/productos
│   ├── admin.py               ← registra modelos en el panel admin
│   └── templates/
│       └── estudiantes/
│           ├── home.html                  ← página principal
│           ├── registro_estudiante.html   ← formulario crear estudiante
│           ├── lista_estudiantes.html     ← listar estudiantes
│           ├── registro_producto.html     ← formulario crear producto
│           ├── lista_productos.html       ← listar + editar + eliminar
│           └── editar_producto.html       ← formulario editar producto
│
└── db.sqlite3                 ← base de datos (se genera con migrate)
```

---

## 📖 Flujo explicado (según diapositivas)

```
Cliente (Browser)
      ↓
    URL
      ↓
  View (Python)     ← lógica de negocio aquí
      ↓
Template (HTML)     ← presentación aquí
      ↓
  Response          ← HTML al navegador
```

**Capas:**
- **Lógica** → Python (views.py)
- **Presentación** → HTML (templates)
- **Interacción** → JavaScript (dentro del HTML)
- **Datos** → ORM → SQLite (models.py)
