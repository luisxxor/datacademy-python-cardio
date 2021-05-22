if __name__ == '__main__':
    print('Ingrese el numero de la conversion que desea realizar')
    print('1 - Si desea transformar millas a kilometros')
    print('2 - Si desea transformar kilometros a millas')
    opcion = int(input(''))
    if opcion != 1 and opcion != 2:
        raise Exception('Esa opcion no es valida')

    millas_por_km = 1.609344

    tasa = millas_por_km if opcion == 1 else 1 / millas_por_km

    nombre_unidad = 'las millas' if opcion == 1 else 'los kilometros'
    unidad = float(input(f'\nInserte {nombre_unidad} a convertir: '))
    resultado = round(unidad * tasa, 2)
    
    resultado_unidad = 'kilometros' if opcion == 1 else 'millas'
    print(f'El resultado es {resultado} {resultado_unidad}')


