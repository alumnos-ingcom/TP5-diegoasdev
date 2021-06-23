################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def compara_listas(lista1, lista2):
    """Retorna True si un par de listas contienen los mismos elementos 
        que pueden estar estén ubicados en diferentes posiciones
    """
    orden1 = 0
    orden2 = 0
    removido = False
    while lista1 != [] and orden1 < len(lista1):
        while lista2 != [] and orden2 < len(lista2) and not removido:
            if lista1[orden1] == lista2[orden2]:
                lista2.pop(orden2)
                removido = True
            orden2 = orden2 + 1
        if not removido:
            return False
        orden1 = orden1 + 1
        orden2 = 0
        removido = False

    if lista2 != []:
        return False

    return True


def prueba():
    si_o_no = ""
    lista1 = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    lista2 = [7, 2, 3, 4, 4, 4, 4, 5, 6, 1]
    print(f"{lista1} y {lista2}")
    if not compara_listas(lista1, lista2):
        si_o_no = "no "
    print(f"\t{si_o_no}contienen los mismos elementos")
    si_o_no = ""
    lista1 = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    lista2 = [7, 2, 3, 4, 5, 6, 1]
    print(f"{lista1} y {lista2}")
    if not compara_listas(lista1, lista2):
        si_o_no = "no "
    print(f"\t{si_o_no}contienen los mismos elementos")
    si_o_no = ""
    lista1 = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    lista2 = [7]
    print(f"{lista1} y {lista2}")
    if not compara_listas(lista1, lista2):
        si_o_no = "no "
    print(f"\t{si_o_no}contienen los mismos elementos")


if __name__ == "__main__":
    prueba()
