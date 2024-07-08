# 1. Cree un programa que permita clasificar a un usuario en un rango de edad como se indica en la siguiente tabla.

edad = int(input('Ingrese su edad: '))

if (edad >=0 and edad <=5) :
    print("Prinera Infancia")
elif (edad>=6 and edad<=11):
    print("Infancia")
elif (edad>=12 and edad<=14):
    print("Adolescencia")
elif (edad>=15 and edad<=26):
    print("Juventud")
elif (edad>=27 and edad<=59):
    print("Adultez")
elif (edad>=60 ):
    print("Persona Mayor")
else:
    print("No hay ningun rango de edad")