# Escribe un programa que verifique si una lista está ordenada de forma ascendente.

lista =[1,2,3,5]

# Variable para almacenar si la lista está ordenada
ordenada = True

# Itera a través de la lista y compara cada elemento con el siguiente
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break  # Termina el bucle si encuentra que la lista no está ordenada

# Imprime el resultado
if ordenada:
    print("La lista está ordenada en forma ascendente.")
else:
    print("La lista no está ordenada en forma ascendente.")