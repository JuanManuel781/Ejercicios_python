# Realice un programa que consecutivamente pida ingresar dos valores para realizar
# operaciones matemáticas y muestre el resultado en consola.

#SUMA
nombre_usuario= input('Ingrese su nombre: ')
numero_suma_uno = int(input(f'{nombre_usuario} ingrese el primero numero: '))
numero_suma_dos = int(input(f'{nombre_usuario} ingrese el Segundo numero: '))
resultado_suma = numero_suma_uno + numero_suma_dos

print(f'{nombre_usuario}, el resultado de la suma es: {resultado_suma} ' )

#RESTA
numero_resta_uno = int(input(f'{nombre_usuario} ingrese el primero numero: '))
numero_resta_dos = int(input(f'{nombre_usuario} ingrese el Segundo numero: '))
resultado_resta = numero_resta_uno - numero_resta_dos

print(f'{nombre_usuario}, el resultado de la resta es: {resultado_resta} ' )

#MULTIPLICACION
numero_multiplicacion_uno = int(input(f'{nombre_usuario} ingrese el primero numero: '))
numero_multiplicacion_dos = int(input(f'{nombre_usuario} ingrese el Segundo numero: '))
resultado_multiplicacion = numero_multiplicacion_uno * numero_multiplicacion_dos

print(f'{nombre_usuario}, el resultado de la multiplicacion es: {resultado_multiplicacion} ' )

#DIVISION
numero_division_uno = int(input(f'{nombre_usuario} ingrese el primero numero: '))
numero_division_dos = int(input(f'{nombre_usuario} ingrese el Segundo numero: '))
resultado_division = numero_division_uno / numero_division_dos

print(f'{nombre_usuario}, el resultado de la division es: {resultado_division} ' )

#DIVISION ENTERA
numero_division1_uno = int(input(f'{nombre_usuario} ingrese el primero numero: '))
numero_division1_dos = int(input(f'{nombre_usuario} ingrese el Segundo numero: '))
resultado_division1 = numero_division1_uno // numero_division1_dos

print(f'{nombre_usuario}, el resultado de la division entera es: {resultado_division1} ' )

#MODULO
numero_modulo_uno = int(input(f'{nombre_usuario} ingrese el primero numero: '))
numero_modulo_dos = int(input(f'{nombre_usuario} ingrese el Segundo numero: '))
resultado_modulo = numero_modulo_uno % numero_modulo_dos

print(f'{nombre_usuario}, el resultado de la multiplicacion es: {resultado_modulo} ' )

#POTENCIA
numero_potencia_uno = int(input(f'{nombre_usuario} ingrese la base: '))
numero_potencia_dos = int(input(f'{nombre_usuario} ingrese el exponente: '))
resultado_potencia = numero_potencia_uno ** numero_potencia_dos

print(f'{nombre_usuario}, el resultado de la potencia es: {resultado_potencia} ' )


