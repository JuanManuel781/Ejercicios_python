numero_uno= int (input('Escriba un numero: '))
estado = True

while estado:
    numero_dos= int (input(f'Escriba un numero mayor {numero_uno}: '))
    if numero_dos > numero_uno:
        numero_uno = numero_dos
    else:
        print("El número ingresado no es mayor que el anterior.")
        continuar = False 