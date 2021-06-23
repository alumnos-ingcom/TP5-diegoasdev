################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def promedio_movil(lista, cantidad):
    orden = 0
    promedio = 0
    sumandos = 0
    promedios = []
    while orden < len(lista):
        if sumandos == cantidad:
            promedio = promedio / cantidad
            promedios.append(promedio)
            sumandos = 0
            orden = orden - cantidad + 1
            promedio = 0
        promedio = promedio + lista[orden]
        sumandos = sumandos + 1
        orden = orden + 1
    return promedios



def prueba():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    cantidad = 3
    print(f"Promedio movil de {lista} segun {cantidad} terminos")
    print(promedio_movil(lista, cantidad))
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    cantidad = 4
    print(f"Promedio movil de {lista} segun {cantidad} terminos")
    print(promedio_movil(lista, cantidad))

if __name__ == "__main__":
    prueba()

