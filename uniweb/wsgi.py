"""
Punto de entrada WSGI para servidores de producción.
Para desarrollo local se usa: python manage.py runserver
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uniweb.settings")
application = get_wsgi_application()
