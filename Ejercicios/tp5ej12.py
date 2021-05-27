################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingresarEntero

def compararListas(lista1, lista2):
    """Compara dos listas y retorna True si tienen los mismos elementos"""
    bandera = True
    if len(lista1) == len(lista2): #Si las listas tienen la misma cantidad de elementos las compara
        for elemento in lista1:
            for elemento2 in lista2:
                if elemento == elemento2:
                    bandera = True
                    break
                else:
                    bandera = False
            if bandera == False:
                break
    else:
        bandera = False
    return bandera

def prueba():
    lista1 = []
    lista2 = []
    cantElementos = ingresarEntero("Ingrese la cantidad de elementos de la lista 1 ")
    for i in range(cantElementos):
        lista1 += input(f"Ingrese el elemento {i+1} de la lista 1: ")
    cantElementos = ingresarEntero("Ingrese la cantidad de elementos de la lista 2 ")
    for i in range(cantElementos):
        lista2 += input(f"Ingrese el elemento {i+1} de la lista 2: ")
    if compararListas(lista1, lista2) == True:
        print("Las listas contienen los mismos elementos!")
    else:
        print("Las listas no contienen los mismos elementos!")



if __name__ == "__main__":
    prueba()
