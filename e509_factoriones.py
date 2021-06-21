################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################

def productoria(numero):
    resultado = numero
    while numero > 2:
        resultado = resultado * (numero - 1)
        numero = numero - 1
    return resultado

def es_factorion(numero, factoriales):
    suma = 0
    digitos = []
    for digito in str(numero):
        digitos.append(digito)
        suma = suma + factoriales[int(digito)]
    if suma == numero:
        return True
    return False


def factoriones_menores_a_1499999():
    factoriales = [1]
    for orden in range(1,10):
        factoriales.append(productoria(orden))

    factoriones = []
    for numero in range(1, 1500000):
        if es_factorion(numero, factoriales):
            factoriones.append(numero)
    return factoriones


def prueba():
    print(" *** Factoriones hasta el 1.499.999 ***")
    orden = 1
    for factorion in factoriones_menores_a_1499999():
        print(f"\t{orden}. {factorion}")
        orden = orden + 1
    print("")

if __name__ == "__main__":
    prueba()

