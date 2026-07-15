from validators.yaml_reader import leer_yaml
from validators.configmap_validator import validar_configmap

def main():
    print("===================================")
    print("      ConfigGuardian iniciado")
    print("===================================")

    ruta_configmap  = "config/configmap-generico.yaml"
    config = leer_yaml(ruta_configmap)

    print("===== CONFIGMAP LEÍDO =====")
    print("\nVariables encontradas:\n")
    data = validar_configmap(config)

    for clave, valor in data.items():
        print(clave, "=", valor)


if __name__ == "__main__":
    main()