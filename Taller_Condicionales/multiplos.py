# Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

primer_numero = int(input('Ingrese el primer numero entero: '))
segundo_numero = int(input('Ingrese el segundo numero entero: '))

if(primer_numero >segundo_numero):
    if(primer_numero %2 ==0):
        print(f'El {primer_numero} es multiplo de {segundo_numero}')
    else:
        print(f'el numero {primer_numero} no es multiplo de {segundo_numero}')
elif(segundo_numero >primer_numero):
    if(segundo_numero %2 ==0):
        print(f'El {segundo_numero} es multiplo de {primer_numero}')
    else:
        print(f'el numero {segundo_numero} no es multiplo de {primer_numero}')
else:
    print('Los numeros ingresados no son validos')