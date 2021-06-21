################
# Diego MINGORANCE - @diegoasdev
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################


# Reemplazar por las funciones del ejercicio
def parentesis_balanceados(texto, parentesis):
    """Devuelve True si los parentesis estan balanceados y
        False si no lo estan. Requiere un abre parentesis del 
        tipo que se quiera evaluar - admite: (, [ o {"""
    if parentesis == "(":
        cierre = ")"
    elif parentesis == "[":
        cierre = "]"
    else:
        cierre = "}"
    balance = 0
    for caracter in texto:
        if caracter == parentesis:
            balance = balance + 1
        elif caracter == cierre:
            balance = balance - 1
            if balance < 0:
                break
    if balance == 0:
        return True
    return False

def auxiliar_de_prueba(texto, parentesis):
    if parentesis_balanceados(texto, parentesis):
        es_o_no_es = f"\tTiene las/los {parentesis} balanceados"
    else:
        es_o_no_es = f"\tNo tiene las/los {parentesis} balanceados"
    return es_o_no_es

def prueba():
    texto = "{FDSAasdf}"
    parentesis = "{"
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")
    texto = "[]"
    parentesis = "["
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")
    texto = "()()"
    parentesis = "("
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")
    texto = "[[][]]"
    parentesis = "["
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")
    texto = "]["
    parentesis = "["
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")
    texto = "][{][}"
    parentesis = "{"
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")
    texto = "[]][[]"
    parentesis = "["
    es_o_no_balanceado = auxiliar_de_prueba(texto, parentesis)
    print(f"\tEl siguiente texto:\n{texto}\n{es_o_no_balanceado}\n")

if __name__ == "__main__":
    prueba()

