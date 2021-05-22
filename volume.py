import math

def volumen_cilindro(altura, radio, decimales=2):
    area_circulo = math.pi * radio**2
    return round(area_circulo * altura, decimales)

if __name__ == '__main__':
    altura = float(input('Inserte la altura del cilindro: '))
    radio = float(input('Inserte el radio del cilindro: '))
    resultado = volumen_cilindro(altura, radio)

    print(f'\nEl volumen del cilindro es: {resultado}')
