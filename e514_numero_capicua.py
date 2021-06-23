################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def es_capicua(natural):
    posicion = 0
    cadena = str(natural)

    while posicion < int(len(cadena) / 2):
        if cadena[posicion] != cadena[-posicion-1]:
            return False
        posicion = posicion + 1

    return True


def prueba():
    natural = 234
    es_o_no = ""
    if not es_capicua(natural):
        es_o_no = "no "
    print(f"\t{natural} {es_o_no}es capicua")
    natural = 2
    es_o_no = ""
    if not es_capicua(natural):
        es_o_no = "no "
    print(f"\t{natural} {es_o_no}es capicua")
    natural = 2334
    es_o_no = ""
    if not es_capicua(natural):
        es_o_no = "no "
    print(f"\t{natural} {es_o_no}es capicua")
    natural = 232
    es_o_no = ""
    if not es_capicua(natural):
        es_o_no = "no "
    print(f"\t{natural} {es_o_no}es capicua")
    natural = 2332
    es_o_no = ""
    if not es_capicua(natural):
        es_o_no = "no "
    print(f"\t{natural} {es_o_no}es capicua")


if __name__ == "__main__":
    prueba()

