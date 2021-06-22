################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def dec_2_bin(natural):
    """Recibe un numero natural y devuelve su version binaria
        como cadena de caracteres
    """
    binario = ""
    while natural > 0:
        if natural % 2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario 
            natural = natural - 1
        natural = natural / 2
    return binario


def bin_2_dec(binario):
    """Recibe un binario como cadena de caracteres y devuelve su 
        version en numero natural
    """
    natural = 0
    digitos = len(binario) - 1
    for digito in binario:
        tmpDigitos = digitos
        tmpNatural = 1
        if digito == "1":
            while tmpDigitos > 0:
                tmpNatural = tmpNatural * 2 
                tmpDigitos = tmpDigitos - 1
            natural = natural + tmpNatural
        digitos = digitos - 1
    return natural


def prueba():
    numero = 325
    binario = dec_2_bin(numero)
    print(f"\t{numero} en binario es {binario}")
    numero = bin_2_dec(binario)
    print(f"\t{binario} en decimal es {numero}")
    numero = 14
    binario = dec_2_bin(numero)
    print(f"\t{numero} en binario es {binario}")
    numero = bin_2_dec(binario)
    print(f"\t{binario} en decimal es {numero}")


if __name__ == "__main__":
    prueba()

