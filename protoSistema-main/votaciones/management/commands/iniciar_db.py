from django.core.management.base import BaseCommand
from votaciones.setup_db import inicializar_base_datos

class Command(BaseCommand):
    help = "Inicializa la base de datos ejecutando los scripts SQL"

    def handle(self, *args, **kwargs):
        inicializar_base_datos()
        self.stdout.write(self.style.SUCCESS("Base de datos inicializada correctamente."))
