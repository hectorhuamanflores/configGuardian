from validators.route_validator import validar_ruta
from validators.configmap_validator import validar_configmaps
from reports.report_generator import generar_reporte


def main():

    carpeta_base = "base/config-properties"
    carpeta_proyecto = "proyecto"

    resultado = validar_ruta(
        carpeta_base,
        carpeta_proyecto
    )

    if not resultado["valido"]:

        generar_reporte(resultado)
        return

    resultado = validar_configmaps(
        carpeta_base,
        resultado["configmaps"]
    )

    generar_reporte(resultado)


if __name__ == "__main__":
    main()