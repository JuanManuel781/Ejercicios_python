numero_uno = int(input('Ingrese primero numero: '))
numero_dos = int(input('Ingrese segundo numero: '))

resultado = numero_uno * numero_dos

if(resultado % 2 ==0):
    print("Par")
else:
    print("Impar")