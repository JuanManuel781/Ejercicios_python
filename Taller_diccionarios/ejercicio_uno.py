diccionario = {}

nombre = str(input(f'ingrese su nombre: '))
edad = int (input(f'ingrese su edad: '))
direccion = str(input(f'ingrese su direccion: '))
telefono = int (input(f'ingrese su telefono: '))

diccionario['nombre']= nombre
diccionario['edad']= edad
diccionario['direccion']= direccion
diccionario['telefono']= telefono

print(diccionario)