lista= [1,2,3,4,5,6]

def media(parametro):

    cantidad = len(parametro)
    suma = 0
    for item in parametro :
        suma +=item
        result = suma/cantidad
    return result

result = media(lista)
print(f'la media de la lista es: {result}')