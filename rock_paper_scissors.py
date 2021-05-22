
opciones = ['piedra', 'papel', 'tijeras']

def ppt(jugador_1, jugador_2):
    j1_index = opciones.index(jugador_1.lower())
    j2_index = opciones.index(jugador_2.lower())

    if (j1_index == j2_index):
        return 0

    j1_pierde_si_j2 = j1_index + 1 if j1_index < 2 else 0

    return 2 if j2_index == j1_pierde_si_j2 else 1

if __name__ == '__main__':
    ronda = 1
    finalizado = False
    j1_puntuacion = 0
    j2_puntuacion = 0
    while not finalizado:
        print('-------------------------------------------')
        print(f'Empieza la ronda {ronda}')
        print(f'Jugador 1: {j1_puntuacion} | Jugador 2: {j2_puntuacion}')
        print('-------------------------------------------\n')
        for i in range(0,3):
            opcion_j1 = input('Opción del jugador 1: ')
            if opcion_j1.lower() not in opciones:
                print("Lo siento, esa opcion es invalida")
                print("Intente con 'piedra', 'papel' o 'tijeras'\n")
                if i == 2:
                    print("Demasiados intentos, lo sentimos")
                    quit()
            else:
                break
        
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

        print()
        resultado = ppt(opcion_j1, opcion_j2)

        if (resultado == 0):
            print(f'Ambos jugadores empataron en la ronda {ronda}\n')
        else:
            print(f'El jugador {resultado} ha ganado la ronda {ronda}\n')

            if (resultado == 1):
                j1_puntuacion += 1
            else:
                j2_puntuacion += 1

        if j1_puntuacion > 1:
            print('Ha ganado el jugador 1 al mejor de 3')
            finalizado = True
        elif j2_puntuacion > 1:
            print('Ha ganado el jugador 2 al mejor de 3')
            finalizado = True
        else:
            ronda += 1

