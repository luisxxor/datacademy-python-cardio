import math

def volumen_cilindro(altura, radio, decimales=2):
    # Para calcular el cilindro hay que multiplicar el area de la base
    # Por la altura, entonces se calcula el area de la base con la formula
    # pi por radio al cuadrado
    area_circulo = math.pi * radio**2

    # y luego lo multiplico por la altura y redondeo el valor por un parametro adicional
    # de decimales, dicho parametro tiene un valor por defecto de 2
    return round(area_circulo * altura, decimales)

if __name__ == '__main__':
    # y bueno, aquí es simplemente pedirle al usuario los valores de la altura y el radio
    altura = float(input('Inserte la altura del cilindro: '))
    radio = float(input('Inserte el radio del cilindro: '))

    # llamar a la funcion e imprimir el resultado
    resultado = volumen_cilindro(altura, radio)

    print(f'\nEl volumen del cilindro es: {resultado}')
