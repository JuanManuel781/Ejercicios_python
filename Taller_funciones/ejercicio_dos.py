def area_circulo(radio,altura):
    pi = 3.14159
    calculo = pi  * radio **2

    def volumne_cilindro(radio,altura):
        volumne=pi * radio **2 * altura
        return volumne

    resultado = volumne_cilindro(radio, altura)

    return {'Area':calculo, 'volumen':resultado}

area = area_circulo(5,2)

print(f'el area y volumen es: {area}')