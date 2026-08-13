# El programa lee conf.txt, guarda las transiciones del AFD
# y prueba cada cadena para verificar si termina en un estado final.

import sys

archivo_conf = sys.argv[1] # Se leen los argumentos o parametros para el programa 
archivo_cadenas = sys.argv[2]

transiciones = {}

with open(archivo_conf, "r") as f:
    for linea in f:
        linea = linea.strip()

        if not linea:  # Si la linea esta vacia continua la siguiente 
            continue

        if linea.startswith("estados="):  # Si la linea empieza con estados empieza a leerlos 
            estados = linea.split("=")[1].split(",")

        elif linea.startswith("alfabeto="): # Empieza a leer el alfabeto, por ejemplo a,b 
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
