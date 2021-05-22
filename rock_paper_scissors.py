
opciones = ['piedra', 'papel', 'tijeras']

# Esta función determina cual de los dos jugadores gana
def ppt(jugador_1, jugador_2):

    # Primero obtengo el indice de la opción que escogió cada jugador
    # En referencia a la lista de opciones
    # siendo piedra => 0, papel => 1, tijeras => 2

    j1_index = opciones.index(jugador_1.lower())
    j2_index = opciones.index(jugador_2.lower())

    # Primero, si ambos escogieron la misma opción, hay empate
    # La función devuelve 0
    if (j1_index == j2_index):
        return 0


    # Luego, viendo la posición de los elementos en la lista se puede notar
    # que cada opción pierde contra la que tiene una posición adelante
    # piedra pierde contra papel, papel pierde contra tijeras y tijeras contra piedra
    # entonces puedo determinar si un jugador perdio contra el otro, lo que obviamente
    # significa que el otro ganó
    
    # Entonces lo que hago es ubicar esa opcion que le gana a la del jugador 1
    # entonces la opción que le gana esta justo despues, pero si el jugador 1 escogió
    # la ultima opción de la lista, el siguiente índice estaría fuera de la lista
    # así que el siguiente indice sería el primero de la lista nuevamente
    j1_pierde_si_j2 = j1_index + 1 if j1_index < 2 else 0

    # Ya teniendo el indice de la opción que vence a la del jugador 1
    # Pregunto si el jugador 2 la escogió. si es asi: gana, de lo contrario, pierde.
    return 2 if j2_index == j1_pierde_si_j2 else 1

if __name__ == '__main__':

    # Inicializo el numero de la ronda, mi bandera del ciclo whil[e
    # y las puntuaciones de los jugadores
    ronda = 1
    finalizado = False
    j1_puntuacion = 0
    j2_puntuacion = 0
    while not finalizado:
        # Cada iteración es una ronda, asi que al inicio de cada iteración
        # Imprimo el estado del juego, numero de ronda y puntuacion de cada jugador
        print('-------------------------------------------')
        print(f'Empieza la ronda {ronda}')
        print(f'Jugador 1: {j1_puntuacion} | Jugador 2: {j2_puntuacion}')
        print('-------------------------------------------\n')

        # Aquí lo que hago es obtener la opción que escoge cada jugador, con un ciclo
        # Para que en el caso de que no ingrese una opción válida, tenga hasta 3 intentos
        # De lo contrario finaliza el programa
        for i in range(0,3):
            opcion_j1 = input('Opción del jugador 1: ')
            if opcion_j1.lower() not in opciones:
                print("Lo siento, esa opcion es invalida")
                print("Intente con 'piedra', 'papel' o 'tijeras'\n")
                if i == 2:
                    print("Demasiados intentos, lo sentimos")

                    # Quizas aqui en vez de finalizar el programa debería penalizar al jugador
                    # Dandole un punto al otro jugador y que continue a la siguiente ronda
                    quit()
            else:
                break
        
        # Lo mismo para el jugador 2
        for i in range(0,3):
            opcion_j2 = input('Opción del jugador 2: ')
            if opcion_j2.lower() not in opciones:
                print("Lo siento, esta opcion es invalida")
                print("Intente con 'piedra', 'papel' o 'tijeras'\n")
                if i == 2:
                    print("Demasiados intentos, lo sentimos")
                    quit()
            else:
                break

        # Obtengo el resultado de la ronda actual
        resultado = ppt(opcion_j1, opcion_j2)

        # Y aquí interpreto los resultados
        if resultado == 0:
            # No hay puntos para nadie porque empataron
            print(f'\nAmbos jugadores empataron en la ronda {ronda}\n')
        else:
            # Si no empataron:
            print(f'\nEl jugador {resultado} ha ganado la ronda {ronda}\n')
            
            if resultado == 1:
                j1_puntuacion += 1
            else:
                j2_puntuacion += 1

        # Si la puntuación de uno de los jugadores es mayor a 1, es porque ha ganado 2 partidas
        # Lo que hace que haya ganado al mejor de 3, asi que muestra el mensaje y marca el flag
        # Para cerrar el ciclo
        if j1_puntuacion > 1:
            print('Ha ganado el jugador 1 al mejor de 3')
            finalizado = True
        elif j2_puntuacion > 1:
            print('Ha ganado el jugador 2 al mejor de 3')
            finalizado = True
        else:
            # En el caso de que ninguno de los dos jugadores haya ganado, lo unico que hago es
            # Incrementar el numero de la ronda antes de que el ciclo se repita
            ronda += 1

