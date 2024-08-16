
lista = ["1", "juan", "3", True, "14.4", "45", "Hola", "12", ["Hola", "mundo"]]
nueva_lista = []

for item in lista :
    try:
        entero = int(item)
        nueva_lista.append(entero)
        
    except (ValueError, TypeError):
        print('Valor no se puede pasar a int')
        nueva_lista.append(item)
        
for valor in nueva_lista:
    print(f'{valor} {type(valor)}')