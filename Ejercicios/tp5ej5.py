################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def inversionMayusculas(texto):
    texto = texto.swapcase()
    return texto

def prueba():
    """Toda la interacción con el usuario va acá"""
    texto = "Hola Mundo"
    texto = inversionMayusculas(texto)
    print(texto)

if __name__ == "__main__":
    prueba()