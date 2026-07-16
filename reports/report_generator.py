def generar_reporte(resultado):

    print("\n====================================")
    print("        CONFIG GUARDIAN")
    print("====================================\n")

    print(resultado["mensaje"])
    print()

    if "errores" in resultado:

        for error in resultado["errores"]:

            print(f"❌ {error}")

    if "configmaps" in resultado:

        for configmap in resultado["configmaps"]:

            if configmap.get("existe", True):

                print(f"✅ {configmap['archivo']}")

            else:

                print(f"❌ {configmap['archivo']}")
                print(f"   Esperado: {configmap['ruta_esperada']}")

    print("\n====================================")