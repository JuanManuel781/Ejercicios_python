# Diccionario de frutas con precios
frutas = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}

# Solicitar al usuario que ingrese el nombre de la fruta
fruta = input('Ingrese el nombre de una fruta: ').strip().lower()

# Solicitar al usuario que ingrese el número de kilos
try:
    kilos = float(input('Ingrese número de kilos: '))
except ValueError:
    print('Por favor, ingrese un número válido para los kilos.')
    exit()

# Inicializar una variable para verificar si la fruta está disponible
fruta_disponible = False

# Recorrer el diccionario para encontrar el precio de la fruta
for fruta1, precio in frutas.items():
    if fruta == fruta1:
        fruta_disponible = True
        resultado = precio * kilos
        print(f'El valor de {kilos} kilos de {fruta} es ${resultado:.2f}')
        break  # Salir del bucle si encontramos la fruta

# Mensaje si la fruta no está disponible
if not fruta_disponible:
    print('La fruta no está disponible.')
