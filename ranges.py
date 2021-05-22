if __name__ == '__main__':
    finalizado = False
    while not finalizado:
        lim_inferior = int(input('Inserte el limite inferior: '))
        lim_superior = int(input('Inserte el limite superior: '))

        if lim_inferior > lim_superior:
            print('\nEl limite superior no puede ser menor al limite inferior')
            print('Intente nuevamente \n')
            continue
        
        num_comparar = int(input('Inserte el numero a comparar: '))

        if num_comparar in range(lim_inferior, lim_superior+1):
            print(f'\nEl numero {num_comparar} se encuentra en el rango {lim_inferior} - {lim_superior}')
            finalizado = True
        else:
            print(f'\nEl numero {num_comparar} no se encuentra en el rango {lim_inferior} - {lim_superior}')
            print('Intentelo nuevamente\n')



