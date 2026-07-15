def validar_configmap(config):

    data = config.get("data")

    if data is None:
        print("No se encontró la sección 'data' en el ConfigMap.")
        return None

    return data