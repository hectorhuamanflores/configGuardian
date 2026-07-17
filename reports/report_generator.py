"""
ConfigGuardian
--------------
Responsabilidad:
Mostrar el resultado final de la validación.
"""


def generar_reporte(resultado):

    print("\n========================================")
    print("          CONFIG GUARDIAN")
    print("========================================\n")

    # -----------------------------
    # ESTRUCTURA
    # -----------------------------

    if "estructura" in resultado:

        print("ESTRUCTURA\n")

        for nombre, estado in resultado["estructura"].items():

            if estado:
                print(f"✅ {nombre}")
            else:
                print(f"❌ {nombre}")

        print("\n----------------------------------------\n")

    # -----------------------------
    # MENSAJE GENERAL
    # -----------------------------

    print(resultado["mensaje"])
    print()

    # -----------------------------
    # ERRORES
    # -----------------------------

    if resultado["errores"]:

        print("ERRORES\n")

        for error in resultado["errores"]:

            print(f"❌ {error}")

        print("\n----------------------------------------\n")

    # -----------------------------
    # CONFIGMAPS
    # -----------------------------

    if "configmaps" in resultado:

        print("CONFIGMAPS\n")

        total = len(resultado["configmaps"])
        validos = 0

        for configmap in resultado["configmaps"]:

            if configmap.get("existe", True):

                print(f"✅ {configmap['archivo']}")
                validos += 1

            else:

                print(f"❌ {configmap['archivo']}")
                print(f"   Ruta esperada: {configmap['ruta_esperada']}")

        print("\n----------------------------------------\n")

        print("RESUMEN\n")

        print(f"ConfigMaps encontrados : {total}")
        print(f"ConfigMaps válidos     : {validos}")

    print("\n========================================")