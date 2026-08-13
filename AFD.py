import sys

archivo_conf = sys.argv[1]
archivo_cadenas = sys.argv[2]

transiciones = {}

with open(archivo_conf, "r") as f:
    for linea in f:
        linea = linea.strip()

        if not linea:
            continue

        if linea.startswith("estados="):
            estados = linea.split("=")[1].split(",")

        elif linea.startswith("alfabeto="):
            alfabeto = linea.split("=")[1].split(",")

        elif linea.startswith("inicial="):
            inicial = linea.split("=")[1]

        elif linea.startswith("finales="):
            finales = linea.split("=")[1].split(",")

        else:
            parte1, destino = linea.split("=")
            estado, simbolo = parte1.split(",")
            transiciones[(estado, simbolo)] = destino


def procesar(cadena):
    estado = inicial

    for simbolo in cadena:

        if simbolo not in alfabeto:
            return False

        if (estado, simbolo) not in transiciones:
            return False

        estado = transiciones[(estado, simbolo)]

    return estado in finales


with open(archivo_cadenas, "r") as f:

    for linea in f:

        cadena = linea.strip()

        if procesar(cadena):
            print(cadena, "-> ACEPTADA")
        else:
            print(cadena, "-> RECHAZADA")
