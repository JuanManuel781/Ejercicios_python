asignaturas ={}

numero_asignaturas= int(input(f'ingrese cuantas asignaturas va ingresar: '))

for _ in range(numero_asignaturas):
    asignatura1 = str(input(f'ingrese una asignatura: '))
    creditos1 = int(input(f'ingrese numero de creditos: '))
    

    asignaturas[asignatura1] =creditos1

total_creditos = 0

for asignatura, creditos in asignaturas.items():
    # Mostrar los créditos de la asignatura
    print(f"{asignatura} tiene {creditos} créditos")
    # Acumular los créditos en la variable total_creditos
    total_creditos += creditos

# Mostrar el número total de créditos del curso
print(f"El número total de créditos del curso es: {total_creditos}")

