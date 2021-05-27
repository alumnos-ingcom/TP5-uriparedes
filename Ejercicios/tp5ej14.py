################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingresarEntero

def capicua(numero):
    """retorna True si el numero ingresado es capicua"""
    numString = str(numero)
    for i in range(len(numString)//2):#toma el numero ingresado como un string
        if numString[i] != numString[len(numString)-(i+1)]:
            return False
    return True

def prueba():
    numero = ingresarEntero("Ingrese un numero ")
    if capicua(numero):
        print("El numero es capicua!")
    else:
        print("El numero no es capicua!")


if __name__ == "__main__":
    prueba()
