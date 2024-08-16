lista= [1,2,3,4,5,6]

def media(parametro):
    cuadrados = []
    for item in parametro :
       cuadrados.append(item ** 2)
    return cuadrados

resultado = media(lista)
print(f'El resultado es: {resultado}')