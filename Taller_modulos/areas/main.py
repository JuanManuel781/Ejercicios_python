
import areas

estado = True

while estado:
    print('=====================================')
    print('============ Areas  ============')
    print('=====================================')
    print('1. Triangulo')
    print('2. Rectangulo')
    print('3. Cuadrado')
    print('4. Trapezio')
    print('5. Losango')
    print('6. Circulo')
    print('7. Salir')


    try:
        opcion = int (input('Ingrese que opcion quiere realizar: '))

        if opcion ==1:
            base = input("Ingrese la base del Triangulo: ")
            altura = input("Ingrese la altura del Triangulo: ")
            print(areas.area_triangulo(base, altura))

        elif opcion ==2:
            base = input("Ingrese la base del Rectangulo: ")
            altura = input("Ingrese la altura del Rectangulo: ")
            print(areas.area_rectangulo(base, altura))
        
        elif opcion ==3:
            lado = input("Ingrese el lado del Cuadrado: ")
            print(areas.area_Cuadrado(lado))
        elif opcion ==4:
            base_mayor = input("Ingrese la base mayor del Trapezio: ")
            base_menor = input("Ingrese la base menor del Trapezio: ")
            altura = input("Ingrese la altura del Trapezio: ")
            print(areas.area_Trapezio(base_mayor, base_menor,altura))

        elif opcion ==5:
            diagonal_mayor = input("Ingrese la diagonal mayor del Losango: ")
            diagonal_menor = input("Ingrese la diagonal menor del Losango: ")
            print(areas.area_Losango(diagonal_mayor,diagonal_menor))

        elif opcion ==6:
            radio = input("Ingrese el radio del Circulo: ")
            print(areas.area_Circulo(radio))

        elif opcion == 7:
            estado = False
    
    except (ValueError, TypeError):
        print('=====================================')
        print('la opcion ingresada no existe')
        estado = True
        print('=====================================')

