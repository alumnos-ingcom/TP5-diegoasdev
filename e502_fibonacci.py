################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def fibonacci(enesimo):
    primero = 1
    segundo = 1
    while enesimo > 2:
        tercero = primero + segundo
        primero = segundo
        segundo = tercero
        enesimo = enesimo - 1
    return tercero

def prueba():
    """Toda la interaccion con el usuario va aca"""
    for enesimo in range(3,21):
        termino = fibonacci(enesimo)
        print(f"El termino numero {enesimo} de Fibonacci es {termino}")

if __name__ == "__main__":
    prueba()

