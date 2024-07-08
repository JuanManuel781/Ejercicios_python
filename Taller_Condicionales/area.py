input1 = input('Quiere calcular el área de un triángulo o la de un círculo: ')

if(input1 == 't' or input1 =='T'):
    base = int(input('Ingrese la base del triagulo : '))
    altura = int(input('Ingrese la altura del triagulo : '))
    resultado = (base * altura)/2
    print('el area del triangulo es: ',resultado)
elif(input1 =='c' or input1=='C'):
    radio = int(input('Ingrese el radio del circulo : '))
    numero_pi = 3.141592
    result =  numero_pi * radio
    print("el area del circulo es: ", result)
else:
    print("error no existe esa opcion")