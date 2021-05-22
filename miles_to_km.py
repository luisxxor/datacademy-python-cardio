if __name__ == '__main__':
    print('Ingrese el numero de la conversion que desea realizar')
    print('1 - Si desea transformar millas a kilometros')
    print('2 - Si desea transformar kilometros a millas')
    
    # Obtengo la opcion del usuario y verifico que sea válida
    opciones_validas = [1, 2]
    opcion = int(input(''))
    if opcion not in opciones_validas:
        raise Exception('Esa opción no es válida')

    # Seteo el valor de millas por kilómetros
    millas_por_km = 1.609344

    # Para hacer una sola operación, que sería la multiplicación
    # Lo que debo hacer es crear una tasa, el valor de la tasa depende
    # De la operación que vaya a realizar, si es de millas a kilometros
    # Uso el valor de millas por kilometros, si es de kilometros a millas
    # entonces la tasa sería el inverso multiplicativo de millas por kilometros
    # que es 1 dividido entre millas por kilometros, multiplicar kilometros
    # por esa tasa, seria como dividir, de esa forma siempre multiplico en el codigo
    tasa = millas_por_km if opcion == 1 else 1 / millas_por_km

    # Aqui le pido al usuario que ingrese el valor que desea convertir
    nombre_unidad = 'las millas' if opcion == 1 else 'los kilometros'
    unidad = float(input(f'\nInserte {nombre_unidad} a convertir: '))

    # Y aquí obtengo el resultado y lo redondeo en una sola operación
    resultado = round(unidad * tasa, 2)
    
    # Mostrando el resultado al final
    resultado_unidad = 'kilometros' if opcion == 1 else 'millas'
    print(f'El resultado es {resultado} {resultado_unidad}')


