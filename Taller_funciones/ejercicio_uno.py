def calcularTotal(parametro1, parametro2=21):
    iva = parametro2/100
    calculo_iva = parametro1*iva
    resultado = parametro1 + calculo_iva
    return resultado


resultado = calcularTotal(5000)
print(f'la cantidad aplicado el iva es: $ {resultado}')  
