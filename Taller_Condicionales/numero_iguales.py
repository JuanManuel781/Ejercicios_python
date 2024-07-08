primer_numero = int(input('Ingrese el primer numero : '))
segundo_numero = int(input('Ingrese el segundo numero : '))
tercer_numero = int(input('Ingrese el tercer numero : '))

if(primer_numero == segundo_numero ==tercer_numero):
    print("Los tres numeros son iguales")
elif (primer_numero == segundo_numero or primer_numero == tercer_numero or segundo_numero == tercer_numero):
    print("hay dos numeros iguales")
else:
    print("los tres numeros son diferentes")
