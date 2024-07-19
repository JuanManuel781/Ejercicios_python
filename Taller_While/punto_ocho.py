

estado = True

while estado:
    print('=====================================')
    print('============ CALCULADORA ============')
    print('=====================================')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicar')
    print('4. Division')
    print('5. Par o Impar')
    print('6. Salir')


    suma = int (input('Ingrese que opcion quiere realizar: '))

    if suma == 1:
        numero_uno = int (input('Ingrese primer numero: '))
        numero_dos = int (input('Ingrese segundo numero: '))
        resultado_suma = numero_uno+numero_dos
        print(f'el resultado de la suma es: {resultado_suma}')
    elif suma ==2:
        numero_uno = int (input('Ingrese primer numero: '))
        numero_dos = int (input('Ingrese segundo numero: '))
        resultado_resta = numero_uno-numero_dos
        print(f'el resultado de la resta es: {resultado_resta}')
    elif suma ==3:
        numero_uno = int (input('Ingrese primer numero: '))
        numero_dos = int (input('Ingrese segundo numero: '))
        resultado_multiplicacion = numero_uno*numero_dos
        print(f'el resultado de la multiplicacion es: {resultado_multiplicacion}')
    elif suma ==4:
        numero_uno = int (input('Ingrese primer numero: '))
        numero_dos = int (input('Ingrese segundo numero: '))
        resultado_division = numero_uno/numero_dos
        print(f'el resultado de la division es: {resultado_division}')
    elif suma ==5:
        numero_uno = int (input('Ingrese primer numero: '))
        if numero_uno %2 ==0:
            print(f'el numero {numero_uno} es par')
        else:
            print(f'el numero {numero_uno} es impar')
    elif suma ==6:
        estado = False
    else:
        print('=====================================')
        print('la opcion ingresada no existe')
        estado = False
        print('=====================================')
