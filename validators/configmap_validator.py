from pathlib import Path


def validar_configmaps(carpeta_base, configmaps):

    ruta_base = Path(carpeta_base) / "ms"

    resultado = {
        "valido": True,
        "mensaje": "Todos los ConfigMaps existen en la base.",
        "configmaps": []
    }

    for archivo in configmaps:

        ruta = ruta_base / archivo.name

        existe = ruta.exists()

        resultado["configmaps"].append(
            {
                "archivo": archivo.name,
                "existe": existe,
                "ruta_esperada": str(ruta)
            }
        )

        if not existe:

            resultado["valido"] = False
            resultado["mensaje"] = "Existen ConfigMaps que no están en la base."

    return resultado