################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp5ej1 as soporte

def tribonacci(numero):
    sucesion = [1, 1, 1]
    for i in range(3, numero):
        sucesion.append(sucesion[i-1] + sucesion[i-2] + sucesion[i-3])
    return sucesion[numero-1]

def prueba():
    """Toda la interacción con el usuario va acá"""
    msg = "ingrese un numero entero: "
    numero = soporte.ingresarEntero(msg)
    sucesion = tribonacci(numero)
    print(f"El elemento {numero} de la secuencia es {sucesion}")

if __name__ == "__main__":
    prueba()