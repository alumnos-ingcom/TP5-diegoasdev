################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


def distancia(numero1, numero2):
    distancia = numero1 - numero2
    if distancia < 0:
        distancia = -distancia
    return distancia


def prueba():
    primero = -3
    segundo = 4
    laDistancia = distancia(primero, segundo)
    print(f"La distancia entre {primero} y {segundo} es {laDistancia}")
    primero = -3
    segundo = -14
    laDistancia = distancia(primero, segundo)
    print(f"La distancia entre {primero} y {segundo} es {laDistancia}")
    primero = 3
    segundo = 4
    laDistancia = distancia(primero, segundo)
    print(f"La distancia entre {primero} y {segundo} es {laDistancia}")

if __name__ == "__main__":
    prueba()

