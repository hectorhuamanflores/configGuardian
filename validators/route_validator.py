from pathlib import Path


def validar_ruta(carpeta_base, carpeta_proyecto):

    ruta_base = Path(carpeta_base)
    ruta_proyecto = Path(carpeta_proyecto)

    resultado = {
        "valido": True,
        "mensaje": "Estructura válida.",
        "estructura": {
            "config-properties": False,
            "bd": False,
            "ms": False,
            "config-main.json": False
        },
        "errores": [],
        "configmaps": []
    }

    # Validar carpeta base
    if not ruta_base.exists():

        resultado["valido"] = False
        resultado["mensaje"] = "No existe la carpeta base."
        resultado["errores"].append(str(ruta_base))

        return resultado

    ruta_config = ruta_proyecto / "config-properties"

    # config-properties
    if not ruta_config.exists():

        resultado["valido"] = False
        resultado["mensaje"] = "No existe config-properties."
        resultado["errores"].append(str(ruta_config))

        return resultado

    resultado["estructura"]["config-properties"] = True

    # bd
    ruta_bd = ruta_config / "bd"

    if not ruta_bd.exists():

        resultado["valido"] = False
        resultado["mensaje"] = "No existe la carpeta bd."
        resultado["errores"].append(str(ruta_bd))

        return resultado

    resultado["estructura"]["bd"] = True

    # ms
    ruta_ms = ruta_config / "ms"

    if not ruta_ms.exists():

        resultado["valido"] = False
        resultado["mensaje"] = "No existe la carpeta ms."
        resultado["errores"].append(str(ruta_ms))

        return resultado

    resultado["estructura"]["ms"] = True

    # config-main.json
    ruta_json = ruta_config / "config-main.json"

    if not ruta_json.exists():

        resultado["valido"] = False
        resultado["mensaje"] = "No existe config-main.json."
        resultado["errores"].append(str(ruta_json))

        return resultado

    resultado["estructura"]["config-main.json"] = True

    # Buscar ConfigMaps
    for archivo in ruta_ms.glob("config-properties-ms-*.yaml"):

        resultado["configmaps"].append(archivo)

    return resultado