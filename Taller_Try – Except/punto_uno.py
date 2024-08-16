
# ejercicio 1 
try:
    # Código que podría causar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre la excepción especificada
    print("No se puede dividir por cero.")