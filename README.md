# AFD en Python - Johan Galeno - Andres Coral

## Objetivo 

El objetivo de esta tarea es implementar un **Autómata Finito Determinista (AFD) en Python** que pueda ser configurado mediante un archivo de texto.

El programa recibe dos archivos como parámetros:

- `conf.txt`: contiene la configuración del autómata.
- `cadenas.txt`: contiene las cadenas que serán evaluadas.

El programa debe leer la configuración del AFD, procesar cada cadena símbolo por símbolo y determinar si la cadena es aceptada o rechazada.

---

## Ejercicio 

Para probar el funcionamiento del programa se eligió la expresión regular:

`(a|b)*abb`

Esta expresión representa todas las cadenas formadas por los símbolos `a` y `b` que terminan en `abb`.

### Cadenas aceptadas

- `abb`
- `aabb`
- `abababb`
- `bbbbabb`

### Cadenas rechazadas

- `ab`
- `abba`
- `aba`
- `bbb`

---

## Proceso del AFD

Para representar la expresión `(a|b)*abb` se utilizaron cuatro estados:

- `q0`
- `q1`
- `q2`
- `q3`

Donde:

- `q0` es el estado inicial.
- `q1` representa que se encontró una `a`.
- `q2` representa que se encontró la secuencia `ab`.
- `q3` representa que se encontró la secuencia `abb`.
- `q3` es el estado de aceptación.

### Tabla de transiciones

| Estado actual | Símbolo | Estado siguiente |
|---|---|---|
| q0 | a | q1 |
| q0 | b | q0 |
| q1 | a | q1 |
| q1 | b | q2 |
| q2 | a | q1 |
| q2 | b | q3 |
| q3 | a | q1 |
| q3 | b | q0 |

El programa almacena las transiciones utilizando un diccionario de Python.

Por ejemplo:

`transiciones[("q1", "b")] = "q2"`

Esto significa que si el autómata se encuentra en `q1` y recibe el símbolo `b`, pasa al estado `q2`.

El programa procesa cada cadena de izquierda a derecha. Por cada símbolo leído cambia de estado según las transiciones definidas en `conf.txt`.

Al terminar de procesar la cadena, se verifica si el estado actual pertenece a los estados finales.

---

## Archivos del proyecto

El proyecto contiene los siguientes archivos:

- `AFD.py`
- `conf.txt`
- `cadenas.txt`
- `README.md`

### AFD.py

Contiene el código principal encargado de leer la configuración del autómata y procesar las cadenas.

### conf.txt

Contiene la configuración del AFD.

Ejemplo:

    estados=q0,q1,q2,q3
    alfabeto=a,b
    inicial=q0
    finales=q3

    q0,a=q1
    q0,b=q0
    q1,a=q1
    q1,b=q2
    q2,a=q1
    q2,b=q3
    q3,a=q1
    q3,b=q0

### cadenas.txt

Contiene las cadenas que serán evaluadas.

Ejemplo:

    abb
    aabb
    abababb
    ab
    abba
    bbbbabb

---

## Ejecución

Para ejecutar el programa se utiliza el siguiente comando:

`python AFD.py conf.txt cadenas.txt`

En Windows también se puede utilizar:

`py AFD.py conf.txt cadenas.txt`

---

## Resultados esperados

Al ejecutar el programa se espera obtener:

    abb -> ACEPTADA
    aabb -> ACEPTADA
    abababb -> ACEPTADA
    ab -> RECHAZADA
    abba -> RECHAZADA
    bbbbabb -> ACEPTADA

Estos resultados muestran que el autómata acepta correctamente las cadenas que terminan en `abb` y rechaza las que no cumplen esta condición.

---

## Conclusión

Con esta implementación se logró construir un **Autómata Finito Determinista configurable en Python**.

La configuración del autómata se encuentra separada del código principal mediante el archivo `conf.txt`, lo que permite modificar estados, alfabeto y transiciones sin cambiar directamente el programa.

El ejercicio permite comprender cómo un AFD procesa una cadena carácter por carácter y realiza transiciones entre estados hasta determinar si la cadena pertenece o no al lenguaje definido.
