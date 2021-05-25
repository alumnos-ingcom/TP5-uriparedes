################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingresarEntero
from math import sqrt

def conversionBinario(numero):
    """Recibe un numero y retorna un string con un numero binario de manera inversa (4 = 001)"""
    binario = ""
    while numero > 0:
        if numero%2 == 0:
            numero = numero//2
            binario += "0"
        elif numero%2 == 1:
            numero = numero//2
            binario += "1"
    return binario

def conversionBinarioInverso(numero):
    binario = ""
    potencia = 0
    for posicion in range(int(sqrt(numero)), -1, -1):
        potencia = 2**posicion
        if (numero - potencia) >= 0:
            numero -= 2**posicion
            binario += "1"
        else:
            binario += "0"
    return binario

def conversionDecimalInverso(binario):
    decimal = 0
    contador = 0
    for posicion in range(len(binario)-1, -1, -1):
        if(binario[contador] == "1"):
            decimal += 2**posicion
        contador += 1
    return decimal

def conversionDecimal(binario):
    """Recibe un string binario y devuelve un numero"""
    numero = 0
    for i in range(len(binario)):
        if binario[i] == "1":
            numero = numero + (2**i)
    return numero

def prueba():
    """Toda la interacción con el usuario va acá"""
    numero = ingresarEntero("Ingrese un numero entero ")
    binario = conversionBinario(numero)
    print(f"El numero {numero}, convertido a binario (menor a mayor) es {binario}")
    numero = conversionDecimal(binario)
    print(f"El numero binario {binario}, convertido a decimal es {numero}")
    binario = conversionBinarioInverso(numero)
    print(f"El numero {numero}, convertido a binario (mayor a menor) es {binario}")
    numero = conversionDecimalInverso(binario)
    print(f"El numero binario {binario}, convertido a decimal es {numero}")
    pass

if __name__ == "__main__":
    prueba()
