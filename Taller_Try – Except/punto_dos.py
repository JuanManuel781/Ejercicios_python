# ejercicio 2
try:
    # Código que podría causar una excepción
    lista = [1,2,3,4]
    lista[10]
except IndexError:
    # Código que se ejecuta si ocurre la excepción especificada
    print("Índice fuera del rango de la lista.")