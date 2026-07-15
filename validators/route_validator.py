from pathlib import Path

"""
ConfigGuardian
--------------
Responsabilidad:
Validar que un archivo exista en la estructura base.
"""

def validar_ruta(nombre_archivo, carpeta_base):

    ruta = Path(carpeta_base) / nombre_archivo

    if ruta.exists():