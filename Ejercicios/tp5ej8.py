################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificacion(texto):
    codificado = ""
    for i in range(len(texto)):
        codificado += (chr(ord(texto[i])+13))
    return codificado

def decodificacion(texto):
    codificado = ""
    for i in range(len(texto)):
        codificado += (chr(ord(texto[i])-13))
    return codificado

def prueba():
    texto = codificacion("hola")
    print(texto)
    texto = decodificacion(texto)
    print(texto)

if __name__ == "__main__":
    prueba()