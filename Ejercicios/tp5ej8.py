################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingresarEntero

def rotX(texto, distancia):
    """Recibe un string, y un entero. codificando el string basado en la distancia dada por el entero"""
    codificado = ""
    for i in texto:
        char = ord(i)
        char += distancia
        if(char-distancia >= ord("a") and char-distancia <= ord("z")):
            while char > ord("z"): #en caso de que tenga que dar mas de 1 "vuelta" al cifrado
                char -= 26
        elif(char-distancia >= ord("A") and char-distancia <= ord("Z")):
            while char > ord("Z"): #en caso de que tenga que dar mas de 1 "vuelta" al cifrado
                char -= 26
        elif(char-distancia >= ord("0") and char-distancia <= ord ("9")):
            while char > ord("9"): #en caso de que tenga que dar mas de 1 "vuelta" al cifrado
                char -= 10
        print(f"{i}({ord(i)}) ->{chr(char)}({char}))")
        codificado += chr(char)
    return codificado

def deRotX(texto, distancia):
    codificado = ""
    for i in texto:
        char = ord(i)
        char -= distancia
        if(char+distancia >= ord("a") and char+distancia <= ord("z")):
            while char < ord("a"): #en caso de que tenga que dar mas de 1 "vuelta" al cifrado
                char += 26
        elif(char+distancia >= ord("A") and char+distancia <= ord("Z")):
            while char < ord("A"): #en caso de que tenga que dar mas de 1 "vuelta" al cifrado
                char += 26
        elif(char+distancia >= ord("0") and char+distancia <= ord ("9")):
            while char < ord("0"): #en caso de que tenga que dar mas de 1 "vuelta" al cifrado
                char += 10
        print(f"{i}({ord(i)}) ->{chr(char)}({char}))")
        codificado += chr(char)
    return codificado


def prueba():
    texto = input("ingrese un texto a cifrar ")
    distancia = ingresarEntero("Ingrese una distancia para el cifrado ")
    texto = rotX(texto, distancia)
    print(texto)
    texto = deRotX(texto, distancia)
    print (texto)


if __name__ == "__main__":
    prueba()
