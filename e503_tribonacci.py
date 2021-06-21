################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def tribonacci(enesimo):
    primero = 1
    segundo = 1
    tercero = 1
    while enesimo > 3:
        cuarto = primero + segundo + tercero
        primero = segundo
        segundo = tercero
        tercero = cuarto
        enesimo = enesimo - 1
    return cuarto

def prueba():
    """Toda la interaccion con el usuario va aca"""
    for enesimo in range(4,21):
        termino = tribonacci(enesimo)
        print(f"El termino numero {enesimo} de Tribonacci es {termino}")

if __name__ == "__main__":
    prueba()

