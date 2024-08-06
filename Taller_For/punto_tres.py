# Escribe un programa que cuente cuántas veces aparece un elemento específico en una lista.

lista = [1,2,3,4,3,3,5]
elemento = 3 
igual = 0

for num in lista :
    if elemento == num:
        igual +=1


print(f'El elemento {elemento} aparece {igual} veces en la lista')

