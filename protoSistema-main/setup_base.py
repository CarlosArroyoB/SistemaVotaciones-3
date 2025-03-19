import os
import django

# Establecer la configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prueba_tecnica.settings")
django.setup()


from django.db import connection

def ejecutar_sql_desde_archivo(archivo_sql):
    """Lee y ejecuta un archivo SQL en la base de datos."""
    if not os.path.exists(archivo_sql):
        raise FileNotFoundError(f"El archivo {archivo_sql} no existe: {archivo_sql}")

    with open(archivo_sql, "r", encoding="utf-8") as archivo:
        sql_script = archivo.read()

    with connection.cursor() as cursor:
        cursor.execute(sql_script)

def crear_tablas():
    """Ejecuta el script SQL que crea las tablas si no existen."""
    ejecutar_sql_desde_archivo("votaciones/sql_scripts/crear_tablas.sql")

def insertar_votante():
    """Ejecuta el script SQL que crea los procedimientos almacenados si no existen."""
    ejecutar_sql_desde_archivo("votaciones/sql_scripts/insertar_votante.sql")

if __name__ == "__main__":
    crear_tablas()
    insertar_votante()
