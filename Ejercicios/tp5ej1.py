################
# Maximiliano Uriel Paredes - @uriparedes
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingresarEntero(mensaje):
    """Esta funcion muestra un mensaje y agrega la # para indicar el ingreso de un numero entero"""
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero entero!") from err
    return entero

def esPar(numero):
    while (numero > 0):
        numero -= 2
    if (numero == 0):
        return True
    return False

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def prueba():
    """Toda la interacción con el usuario va acá"""
    msg = "Ingrese un numero entero: "
    numero = ingresarEntero(msg)
    if(esPar(numero)):
        print(f"{numero} es par!")
    else:
        print(f"{numero} es impar!")

if __name__ == "__main__":
    prueba()