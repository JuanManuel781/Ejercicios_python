import math


# area de Triangulo
def area_triangulo(base, altura):
    try:
        base = float(base)
        altura = float(altura)
        
        if base <= 0 or altura <= 0:
            return "La base y la altura deben ser valores mayores que cero."
        
        return f"El área del triángulo es: {(base * altura) / 2}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."
    
# area de Rectangulo
def area_rectangulo(base, altura):
    try:
        base = float(base)
        altura = float(altura)
       
        if base <= 0 or altura <= 0:
            return "La base y la altura deben ser valores mayores que cero."
        
        return f"El área del rectangulo es: {(base * altura)}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."
    
# area de Cuadrado
def area_Cuadrado(lado):
    try:
        lado = float(lado)
       
        if lado <= 0 :
            return "El valor del lado debe ser mayor que cero."
        
        return f"El área del cuadrado es: {(lado **2)}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."


# area de Trapezio
def area_Trapezio(base_mayor, base_menor,altura):
    try:
        base_mayor = float(base_mayor)
        base_menor = float(base_menor)
        altura = float(altura)
       
        if base_mayor <= 0 and base_mayor<=0 and base_menor<=0 :
            return "los valores deben ser mayores que cero."
        
        return f"El área del Trapezio es: {((base_mayor+base_menor)*altura)/2}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."

# area de Losango
def area_Losango(diagonal_mayor, diagonal_menor):
    try:
        diagonal_mayor = float(diagonal_mayor)
        diagonal_menor = float(diagonal_menor)

       
        if diagonal_mayor <= 0 and diagonal_menor<=0  :
            return "los valores deben ser mayores que cero."
        
        return f"El área del Losango es: {(diagonal_mayor*diagonal_menor)/2}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."
    
# area de Circulo
def area_Circulo(radio):
    try:
        radio = float(radio)
        

       
        if radio <= 0  :
            return "los valores deben ser mayores que cero."
        
        return f"El área del Circulo es: {(math.pi *(radio **2))}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."

