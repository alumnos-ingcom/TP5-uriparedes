################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingresarEntero
from math import sqrt

def conversionBinario(numero):
    """Recibe un numero y retorna un string con un numero binario de menor a mayor (4 = 001)"""
    binario = ""
    while numero > 0: #Mientras que el numero ingresado sea mayor a 0, va agregando digitos
        if numero%2 == 0: # Si el numero es par, agrega 0 y divide al numero en dos (division entera)
            numero = numero//2
            binario += "0"
        elif numero%2 == 1: #Si el numero es impar, agrega 1 y lo divide en 2
            numero = numero//2
            binario += "1"
    return binario

# realizo un pequeño ejemplo para entender mejor la idea de dividir por dos el numero:
# ingreso el numero 15:
# numero  binario numero dividido
# 15      "1"     7
# 7       "11"     3
# 3       "111"    1
# 1       "1111"   0

def conversionBinarioInverso(numero):
    """Toma un numero y retorna un string con un numero binario ordenado de mayor a menor (4 = 100)"""
    binario = ""
    potencia = 0
    limit = limite(numero) # calcula cual es el numero mas grande que pueda tener el nro binario
    for posicion in range(limit , -1, -1): # comienza la conversion a binario desde el numero mas grande hasta 0
        potencia = 2**posicion # Un numero binario es igual a 2^n, siendo n la posicion del numero
        if numero >= potencia: # Si la variable potencia es menor o igual al numero ingresado, realiza la resta y agrega 1 al nro binario
            numero -= potencia
            binario += "1"
        else: #Si la potencia es mayor al numero, agrega 0
            binario += "0"
    return binario

def conversionDecimalInverso(binario):
    """Recibe un string con un numero binario y devuelve un numero entero que lo representa"""
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

def limite(numero):
    """recibe un numero y devuelve el exponencial binario mas grande posible"""
    limit = int(sqrt(numero))
    reductor = 0
    while(2**limit > numero):
        reductor += 1
        limit = int(sqrt(numero - reductor))
    return limit

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
