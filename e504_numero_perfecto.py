################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio


def numero_perfecto(natural):
    """Devuelve True si el numero natural recibido es un numero perfecto,
        es decir, si la suma de sus divisores excluyendo al mismo es igual
        al numero natural ingresado
    """
    suma_aliquota = 1
    divisor = 2
    while divisor <= natural/2 and suma_aliquota <= natural:
        if natural % divisor == 0:
            suma_aliquota = suma_aliquota + divisor
        divisor = divisor + 1
    if suma_aliquota == natural:
        return True
    return False

def prueba():
    """Toda la interaccion con el usuario va aca"""
    for numero in range(3,10000):
        if numero_perfecto(numero):
            print(f"El numero {numero} es un numero perfecto")

if __name__ == "__main__":
    prueba()

