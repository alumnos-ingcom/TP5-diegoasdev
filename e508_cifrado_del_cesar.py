################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################

def maxCarRot():
    return 126


def minCarRot():
    return 32


def esCaracterRotable(caracter):
    if ord(caracter) >= minCarRot() and ord(caracter) <= maxCarRot():
        return True
    else:
        return False


def cifradoCesar(texto, rotacion, descifrar):
    """Realiza el cifrado per se. Recibe el texto a (des)cifrar, la cantidad 
            de rotaciones y un entero que debe ser 0 para cifrar o 1 para descifrar
    """
    if descifrar:
        rotacion = -rotacion
    salida = ""
    for caracter in texto:
        # Si es un caracter rotable lo rota segun la rotacion indicada
        # entre minCarRot y maxCarRot
        # En este caso se eligio el espacio como minCarRot y el caracter ~
        # como maxCarRot
        if esCaracterRotable(caracter):
            caracter = chr(((ord(caracter) - minCarRot() + rotacion)
                            % (maxCarRot() - minCarRot() + 1)) + minCarRot())
        # Si no es un caracter rotable, se lo utiliza como viene
        salida = salida + caracter
    return salida


def cifrarCesar(texto, rotacion):
    return cifradoCesar(texto, rotacion, 0)


def descifrarCesar(texto, rotacion):
    return cifradoCesar(texto, rotacion, 1)


def prueba():
    """Pruebas"""
    texto = "Que es lo que esta pasando en todo esto? 3 de -4.5"
    rotacion = 500001234
    cifrado = cifrarCesar(texto, rotacion)
    descifrado = descifrarCesar(cifrado, rotacion)
    print(f"Original:   {texto}")
    print(f"Cifrado:    {cifrado}")
    print(f"Descifrado: {descifrado}")


if __name__ == "__main__":
    prueba()
