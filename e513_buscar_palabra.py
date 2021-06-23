################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


def buscar_palabra(texto, palabra):
    orden1 = 0
    orden2 = 0
    ubicacion = 0
    posible_encuentro = False
    while orden1 < len(texto):
        if palabra[orden2] == texto[orden1]:
            if posible_encuentro == False:
                ubicacion = orden1
            posible_encuentro = True
            if orden2 == len(palabra)-1:
                return ubicacion
            orden2 = orden2 + 1
        else:
            posible_encuentro = False
            orden2 = 0
        orden1 = orden1 + 1
    raise PalabraNoEncontrada(f"No se encontro {palabra} en el texto")


class PalabraNoEncontrada(Exception):
    """Esta es la excepcion cuando no se encuentra la palabra en el texto"""
    pass
    

def prueba():
    texto = "Este es un texto cualquiera"
    palabra = "to cu"
    ubicacion = buscar_palabra(texto, palabra)
    print(f"{texto}\n\t{palabra} se encontro en {ubicacion}")
    texto = "Este es un texto cualquiera"
    palabra = "toac"
    ubicacion = buscar_palabra(texto, palabra)
    print(f"{texto}\n\t{palabra} se encontro en {ubicacion}")

if __name__ == "__main__":
    prueba()

