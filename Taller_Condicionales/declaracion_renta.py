# Los valores para la declaración de la renta en un determinado país son los siguientes:
#Pregunte el sueldo devengado por el usuario y realice el calculo de cuanto debe pagar el
#usuario según sus ingresos


sueldo = int(input('Ingrese su saldo devengado: '))

if(sueldo>0 and sueldo<10000):
    resultado = sueldo*0.05
    print(f'El 5% de {sueldo} es: {resultado}')
elif (sueldo>=10000 and sueldo<20000):
    resultado = sueldo*0.15
    print(f'El 15% de {sueldo} es: {resultado}')
elif(sueldo>=20000 and sueldo< 35000):
    resultado = sueldo*0.2
    print(f'El 20% de {sueldo} es: {resultado}')
elif(sueldo>=35000 and sueldo<60000):
    resultado = sueldo*0.3
    print(f'El 30% de {sueldo} es: {resultado}')
elif(sueldo>=60000):
    resultado = sueldo*0.45
    print(f'El 45% de {sueldo} es: {resultado}')
else:
    print("Fuera del rango")