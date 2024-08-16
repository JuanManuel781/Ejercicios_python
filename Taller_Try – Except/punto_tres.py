# ejercicio 3
try:
    # Código que podría causar una excepción
    resultado = 10 + '20'
except TypeError:
    # Código que se ejecuta si ocurre la excepción especificada
    print("No se puede sumar un número con una cadena de texto.")