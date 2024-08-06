# Escribe un programa que elimine los elementos duplicados de una lista. 

numeros = [1,2,3,2,4,5,3,6]
sinduplicar=[]
#lista_sin_duplicados = list(set(numeros))
#print(lista_sin_duplicados)

vistos = []
sin_duplicados = []

for num in numeros:
    if num not in vistos:
        sin_duplicados.append(num)
        vistos.append(num)

print("Lista sin duplicados:", sin_duplicados) 