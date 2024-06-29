# Realice los siguientes programas con el uso de operadores lógicos (and, or, not)

# Pide al usuario que ingrese dos números y luego imprime si ambos números son mayores que 10.

numero_uno_mayor = int(input('Ingrese el primer numero: '))
numero_dos_mayor = int(input('Ingrese el segundo numero: '))

print(
    f'Los dos numero son mayores que 10 : {numero_uno_mayor and numero_dos_mayor > 10}')

# Pide al usuario que ingrese dos números y luego imprime si al menos uno de los números es mayor que 10.

numero_uno_mayor_uno = int(input('Ingrese el primer numero: '))
numero_dos_mayor_dos = int(input('Ingrese el segundo numero: '))


print(
    f'Los dos numero son mayores que 10 : {(numero_uno_mayor_uno >10) or (numero_dos_mayor_dos > 10)}')

# Pide al usuario que ingrese un número y luego imprime si el número no es mayor que 10. (Use el operador ‘not’)

numero_uno_1 = int(input('Ingrese el primer numero: '))
if not (numero_uno_1 > 10):
    print("El número", numero_uno_1, "NO es mayor que 10.")
else:
    print("El número", numero_uno_1, "ES es mayor que 10.")

# Pide al usuario que ingrese tres números y luego imprime si el primer número es mayor
# que 5 y el segundo número es menor que 10 o el tercer número es igual a 20.

numero_comparar_uno = int(input('Ingrese el primer numero: '))
numero_comparar_dos = int(input('Ingrese el segundo numero: '))
numero_comparar_tres = int(input('Ingrese el tercer numero: '))

print(
    f'El resultado es : { ((numero_comparar_uno >5) and ((numero_comparar_dos <10) or numero_comparar_tres ==20))}')

# Pide al usuario que ingrese dos números y luego imprime si no es cierto que ambos números son mayores que 10.

numero__uno = int(input('Ingrese el primer numero: '))
numero__dos = int(input('Ingrese el segundo numero: '))


print(f'los dos numeros son mayores : {(numero__uno and numero__dos > 10)}') 
