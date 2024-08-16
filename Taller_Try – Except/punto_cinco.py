

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

    try:
        suma = int (input('Ingrese que opcion quiere realizar: '))
        if suma == 1:
            try:
                numero_uno = int (input('Ingrese primer numero: '))
                numero_dos = int (input('Ingrese segundo numero: '))
                resultado_suma = numero_uno+numero_dos
                print(f'el resultado de la suma es: {resultado_suma}')
            except (ValueError, TypeError):
                 print(f'el tipo de dato no es permitido')        
        elif suma ==2:
            try:
                numero_uno = int (input('Ingrese primer numero: '))
                numero_dos = int (input('Ingrese segundo numero: '))
                resultado_resta = numero_uno-numero_dos
                print(f'el resultado de la resta es: {resultado_resta}')
            except (ValueError, TypeError):
                 print(f'el tipo de dato no es permitido')   
        elif suma ==3:
            try:
                numero_uno = int (input('Ingrese primer numero: '))
                numero_dos = int (input('Ingrese segundo numero: '))
                resultado_multiplicacion = numero_uno*numero_dos
                print(f'el resultado de la multiplicacion es: {resultado_multiplicacion}')
            except (ValueError, TypeError):
                 print(f'el tipo de dato no es permitido')   
        elif suma ==4:
            try:
                numero_uno = int (input('Ingrese primer numero: '))
                numero_dos = int (input('Ingrese segundo numero: '))
                resultado_division = numero_uno/numero_dos
                print(f'el resultado de la division es: {resultado_division}')
            except (ValueError, TypeError):
                 print(f'el tipo de dato no es permitido')   
        elif suma ==5:
            try:
                numero_uno = int (input('Ingrese primer numero: '))
                if numero_uno %2 ==0:
                    print(f'el numero {numero_uno} es par')
                else:
                    print(f'el numero {numero_uno} es impar')
            except (ValueError, TypeError):
                 print(f'el tipo de dato no es permitido')   
        elif suma ==6:
            estado = False
  
    except (ValueError, TypeError):
        print('=====================================')
        print('la opcion ingresada no existe')
        estado = True
        print('=====================================')

    
