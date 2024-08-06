# Escribe un programa que multiplique cada elemento de una lista por 2 y almacene el resultado en una nueva lista.

numeros = [1,2,3,4,5]
numero_multiplicar = 2
total = []


for num in numeros:
    total.append(num*numero_multiplicar)

print(f'Los numeros multiplicados por {numero_multiplicar} son: {total}')