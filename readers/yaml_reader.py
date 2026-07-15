import yaml

def leer_yaml(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = yaml.safe_load(archivo)

    return contenido