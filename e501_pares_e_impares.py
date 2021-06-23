################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def es_par(entero):
    """Se fija si la division por 2 es igual tomando la parte entera"""
    if entero/2 == int(entero/2):
        return True
    else:
        return False


def prueba():
    """Toda la interaccion con el usuario va aca"""
    es_o_no = ""
    numero = 904
    if not es_par(numero):
        es_o_no = "no "
    print(f"El numero {numero} {es_o_no}es par")
    numero = 17
    if not es_par(numero):
        es_o_no = "no "
    print(f"El numero {numero} {es_o_no}es par")


if __name__ == "__main__":
    prueba()
