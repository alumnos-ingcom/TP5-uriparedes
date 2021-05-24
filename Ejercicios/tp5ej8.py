################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def rot13(texto):
    codificado = ""
    for i in texto:
        char = ord(i)
        if(char >= ord("a") and char <= ord("z")):
            if char > ord("m"):
                char -= 13
            else:
                char += 13
        elif(char >= ord("A") and char <= ord("Z")):
            if char > ord("M"):
                char -= 13
            else:
                char += 13
        elif(char >= ord("0") and char <= ord ("9")):
            if(char < ord("7")):
                char += 3
            else:
                char -= 7
        print(f"{i}({ord(i)}) -> {chr(char)}({char}))")
        codificado += chr(char)
    return codificado

def deRot13(texto):
    codificado = ""
    for i in texto:
        char = ord(i)
        if(char >= ord("a") and char <= ord("z")):
            if char > ord("m"):
                char -= 13
            else:
                char += 13
        elif(char >= ord("A") and char <= ord("Z")):
            if char > ord("M"):
                char -= 13
            else:
                char += 13
        elif(char >= ord("0") and char <= ord ("9")):
            if(char < ord("3")):
                char += 7
            else:
                char -= 3
        print(f"{i}({ord(i)}) -> {chr(char)}({char}))")
        codificado += chr(char)
    return codificado


def prueba():
    texto = input("ingrese un texto a cifrar ")
    texto = rot13(texto)
    print(texto)
    texto = deRot13(texto)
    print (texto)


if __name__ == "__main__":
    prueba()