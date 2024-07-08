# Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

actual = int(input('Ingrese el año actual: '))
nuevo = int(input('Ingrese el año alazar: '))


if(actual>nuevo):
    resultado = actual-nuevo
    print(f'han trascurrido {resultado}  años')
else:
    resultado = nuevo - actual
    print(f'faltan  {resultado}  años para llegar {nuevo}')

