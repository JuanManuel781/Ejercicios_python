# Escribe un programa que encuentre el valor máximo en una lista de números.

numeros = [3,7,2,9,5]
max = numeros[0]

for num in numeros:
    if num > max:
        max = num

print(max)