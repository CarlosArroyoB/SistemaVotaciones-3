from django.apps import AppConfig
# from .setup_db import crear_tablas, insertar_votante

class VotacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'votaciones'
    # def ready(self):
    #     crear_tablas()
    #     insertar_votante()