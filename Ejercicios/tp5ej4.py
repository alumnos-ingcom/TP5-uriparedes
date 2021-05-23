################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp5ej1 as soporte

def numPerfecto(numero):
    suma = 0
    for i in range(1, numero):
        if(numero%i == 0):
            suma+= i        
    if(suma == numero):
        return True
    else:
        return False

def prueba():
    """Toda la interacción con el usuario va acá"""
    msg = "ingrese un numero entero: "
    numero = soporte.ingresarEntero(msg)
    if(numPerfecto(numero)):
        print(f"{numero} es un numero perfecto!")
    else:
        print(f"{numero} no es un numero perfecto!")

if __name__ == "__main__":
    prueba()