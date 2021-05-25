################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingresarEntero

def factorion(limite):
    factoriones = []
    for n in range(limite):
        nFactorial = 0
        for numero in str(n):
            nFactorial += factorial(int(numero))
            # print(f"n={n}, numero = {nFactorial}")
        if nFactorial == n:
            print(f"{n} = {nFactorial} es un factorion!")
            factoriones.append(n)
    return factoriones

def factorial(numero):
    """Calcula el factorial de un numero dado"""
    factorial = 1
    for i in range(numero):
        factorial *= i+1
    return factorial

def prueba():
    limite = ingresarEntero("Ingrese un limite para los factoriones")
    lista = factorion(limite)
    print(f"los numeros factoriones son : {lista}")

if __name__ == "__main__":
    prueba()
