if __name__ == '__main__':
    # inicializo la bandera para el ciclo while
    finalizado = False
    while not finalizado:
        # Y en cada iteración el usuario tendrá que setear un limite inferior
        # y uno superior
        lim_inferior = int(input('Inserte el limite inferior: '))
        lim_superior = int(input('Inserte el limite superior: '))

        # Aquí coloco una pequeña validación para evitar que el rango
        # esté invertido, haciendo que el usuario deba ingresar los limites nuevamente

        if lim_inferior > lim_superior:
            print('\nEl limite superior no puede ser menor al limite inferior')
            print('Intente nuevamente \n')
            continue
        
        # Y luego le pido al usuario el numero de comparación
        num_comparar = int(input('Inserte el numero a comparar: '))

        # Para luego preguntar si el numero se encuentra en el rango definido:
        if num_comparar in range(lim_inferior, lim_superior+1):
            # Si es asi, pues le aviso al usuario y cambio la bandera para finalizar el ciclo while
            print(f'\nEl numero {num_comparar} se encuentra en el rango {lim_inferior} - {lim_superior}')i
            finalizado = True
        else:
            # De lo contrario le muestro un mensaje al usuario y le digo que lo intente nuevamente
            # Como no cambio la bandera, el usuario tendrá que repetir toda la iteración
            print(f'\nEl numero {num_comparar} no se encuentra en el rango {lim_inferior} - {lim_superior}')
            print('Intentelo nuevamente\n')



