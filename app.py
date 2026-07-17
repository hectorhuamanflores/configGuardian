from validators.route_validator import validar_ruta
from validators.configmap_validator import validar_configmaps
from reports.report_generator import generar_reporte


def main():

    carpeta_base = "base/config-properties"
    carpeta_proyecto = "proyecto"

    resultado_ruta = validar_ruta(
        carpeta_base,
        carpeta_proyecto
    )

    if not resultado_ruta["valido"]:

        generar_reporte(resultado_ruta)
        return

    resultado_configmaps = validar_configmaps(
        carpeta_base,
        resultado_ruta["configmaps"]
    )

    # Combinar resultados
    resultado_configmaps["estructura"] = resultado_ruta["estructura"]
    resultado_configmaps["errores"] = resultado_ruta["errores"]

    generar_reporte(resultado_configmaps)


if __name__ == "__main__":
    main()