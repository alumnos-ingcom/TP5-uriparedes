################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def balanceo(texto):
    pila = []
    for caracter in texto:
        if caracter == "{" or caracter == "[" or caracter == "(":
            pila.append(caracter)
        elif caracter == "}" or caracter == "]" or caracter == ")":
            if len(pila) == 0:
                return False
            comparar = pila.pop()
            if not (comparar == "{" and caracter == "}" or comparar == "[" and caracter == "]" or comparar == "(" and caracter == ")"):
                return False
    if not pila:
        return True
    else:
        return False

def prueba():
    texto = "[]{{ñ}}{"
    if balanceo(texto) == True:
        print("El texto esta balanceado!")
    else:
        print("El texto no esta balanceado!")

if __name__ == "__main__":
    prueba()