
usuarios = {}
placas=[]
numero_asignaturas= int(input(f'ingrese cuantas asignaturas va ingresar: '))

for _ in range(numero_asignaturas):
    documento = int(input(f'ingrese numero de documento: '))
    nombre = str(input(f'ingrese su nombre: '))
    apellido = str(input(f'ingrese su apellido: '))
    direccion = str(input(f'ingrese su direccion: '))
    telefono = int(input(f'ingrese su telefono: '))
    # pregunta cuantas placas de vehiculo desea ingresar
    vehiculos= int(input(f'ingrese cuantas placas de vehiculo va ingresar: '))
    for _ in range(vehiculos):
         vehiculos= str(input(f'ingrese la placa del vehiculo: '))
         placas.append(vehiculos)

    datos_asignatura = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Direccion':direccion,
        'Telefono':telefono,
        'Placa':placas
    }

    # Agregar la asignatura y los datos al diccionario principal
    usuarios[documento] = datos_asignatura

print(usuarios)
    


