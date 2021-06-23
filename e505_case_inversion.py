################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################

def es_minuscula(letra):
    if ord(letra) >= ord("a") and ord(letra) <= ord("z"):
        return True
    return False


def es_mayuscula(letra):
    if ord(letra) >= ord("A") and ord(letra) <= ord("Z"):
        return True
    return False


def a_mayuscula(letra):
    letra = chr(ord(letra)-ord("a")+ord("A"))
    return letra


def a_minuscula(letra):
    letra = chr(ord(letra)-ord("A")+ord("a"))
    return letra

# Reemplazar por las funciones del ejercicio


def case_inversion(texto):
    salida = ""
    for letra in texto:
        if es_minuscula(letra):
            letra = a_mayuscula(letra)
        elif es_mayuscula(letra):
            letra = a_minuscula(letra)
        salida = salida + letra
    return salida


def prueba():
    mensaje = "Tenemos qUe VEr 17 dE estOs"
    mensaje_invertido = case_inversion(mensaje)
    print(f"{mensaje}\n\tinvertido a:\n{mensaje_invertido}")


if __name__ == "__main__":
    prueba()
