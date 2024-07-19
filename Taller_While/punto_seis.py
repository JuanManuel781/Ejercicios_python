numero_uno= int (input('Ingrese la cantidad de numeros a ser sumados: '))
contador = 0
suma_total=0

while contador <numero_uno:
    numero = int (input(f'Ingrese el numero {contador +1}: '))
    suma_total +=numero
    contador +=1
    

print(f"La suma total de los {numero_uno} números ingresados es: {suma_total}")