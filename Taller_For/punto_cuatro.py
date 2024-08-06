# Escribe un programa que extraiga todos los números pares de una lista y los almacene en una nueva lista.

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(f'Los pares son: {pares}')