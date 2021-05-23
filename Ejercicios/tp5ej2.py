################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp5ej1 as soporte

def fibonacci(numero):
    sucesion = [1, 1]
    for i in range(2, numero):
        sucesion.append(sucesion[i-1] + sucesion[i-2])
    return sucesion[numero-1]
        
def prueba():
    """Toda la interacción con el usuario va acá"""
    msg = "ingrese un numero entero: "
    numero = soporte.ingresarEntero(msg)
    sucesion = fibonacci(numero)
    print(f"El elemento n°{numero} es {sucesion}")

if __name__ == "__main__":
    prueba()