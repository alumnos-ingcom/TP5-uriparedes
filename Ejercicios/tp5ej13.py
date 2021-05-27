################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def buscarPalabra(texto, palabra):
    """Toma dos strings, el primero es un texto y el segundo una palabra, chequea que el segundo este contenido en el primero"""
    resultado = False
    for p in texto.split():
        if palabra == p:
            resultado = True
            break
    return resultado

def prueba():
    with open("texto.txt", "r") as archivo:
        texto = archivo.read().replace("\n", " ")
    print("El texto es:\n" + texto + "\n")
    palabra = input("Ingrese el termino a buscar en el texto: ")
    if buscarPalabra(texto, palabra):
        print(f"{palabra} esta en el texto!")
    else:
        print(f"{palabra} no esta en el texto!")


if __name__ == "__main__":
    prueba()
