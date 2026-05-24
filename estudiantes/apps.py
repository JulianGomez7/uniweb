from django.apps import AppConfig


class EstudiantesConfig(AppConfig):
    # Tipo de campo ID por defecto para los modelos de esta app
    default_auto_field = "django.db.models.BigAutoField"
    # Nombre del paquete (debe coincidir con el nombre de la carpeta)
    name = "estudiantes"
