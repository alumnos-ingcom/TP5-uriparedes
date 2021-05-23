################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(numero1, numero2):
    if numero1 > numero2:
        distancia = numero1 - numero2
    else:
        distancia = numero2 - numero1
    return distancia

def prueba():
    numero = distancia(66.7, -5)
    print(f"La distancia entre los numeros es {numero}")


if __name__ == "__main__":
    prueba()