from django.db import connection
import os

def ejecutar_sql_desde_archivo(archivo_sql):
    """Lee y ejecuta un archivo SQL en la base de datos."""
    ruta_completa = os.path.join(os.path.dirname(__file__), "sql_scripts", archivo_sql)

    with open(ruta_completa, "r", encoding="utf-8") as archivo:
        sql_script = archivo.read()

    with connection.cursor() as cursor:
        cursor.execute(sql_script)

def inicializar_base_datos():
    ejecutar_sql_desde_archivo("crear_tablas.sql")
    ejecutar_sql_desde_archivo("insertar_votante.sql")
    ejecutar_sql_desde_archivo("insertar_candidato.sql")
    ejecutar_sql_desde_archivo("insertar_voto.sql")
