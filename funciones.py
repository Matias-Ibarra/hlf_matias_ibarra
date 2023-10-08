def disparar(jugador, tablero, tablero_disparos, fila=0, columna=0):
    '''
    La función disparar pide al jugador coordenadas del tablero, si coincide con un barco del oponente, se imprime una letra X en el tablero de este último.
    Si las coordenadas coinciden con una casilla vacía, el disparo va al mar, se imprime @ en el tablero del oponente.
    Variables a introducir:
    jugador: nombre introducido por el jugador u ordenador, según de quien sea el turno.
    tablero: array de 10x10 con los barcos correspondientes.
    tablero_disparos: el tablero que se mostrará en pantalla con los disparos ya realizados. En el caso del jugador, el tablero que se vera es un tablero vacio
                      al que se le van agregando los disparos.
    fila: un input efectuado por el usuario en su turno, un valor aleatorio entre 0 y 9 para el ordenador.
    columna: un input efectuado por el usuario en su turno, un valor aleatorio entre 0 y 9 para el ordenador.
    '''

    import numpy as np
    import random
    import os
    import time
    # Si el turno es del ordenador el disparo será aleatorio
    if jugador == "ordenador":
        fila = random.randint(0,9)
        columna = random.randint(0,9)
    # Si el turno es del jugador, se elige donde disparar por un input. Se comprueba que sea una entrada
    # válida, sino se vuelve a ejecutar la función
    else:
        print("\nTurno de disparar, selecciona las coordenadas:\n")
        fila = input("Fila: ")
        try:
            int(fila)
        except:
            print("\nLa fila debe pertenecer al rango (0, 9), intente nuevamente...\n")
            disparar(jugador, tablero, tablero_disparos, fila, columna)
        if int(fila) in range(0, 10):
            fila = int(fila)
        else:
            print("\nLa fila debe pertenecer al rango (0, 9), intente nuevamente...\n")
            disparar(jugador, tablero, tablero_disparos, fila, columna)
        columna = input("Columna: ")
        try:  
            int(columna)
        except:
            print("\nLa columna debe pertenecer al rango (0, 9), intente nuevamente...\n")   
            disparar(jugador, tablero, tablero_disparos, fila, columna)
        if int(columna) in range(0, 10):
            columna = int(columna)
        else:
            print("\nLa columna debe pertenecer al rango (0, 9), intente nuevamente...\n")
            disparar(jugador, tablero, tablero_disparos, fila, columna)
    # Si el disparo va a una casilla vacía del tablero del oponente, se imprime un @ en el tablero a mostrar en pantalla.
    if tablero[fila][columna] == " ":
        if tablero_disparos[fila][columna] == "@":
            print("Ya has disparado a esa casilla, intenta nuevamente")
            time.sleep(0.75)
            disparar(jugador, tablero, tablero_disparos, fila, columna)
        else:
            print("\nDisparo al agua!\n")
            time.sleep(0.75)
            tablero_disparos[fila][columna] = "@"
            return tablero_disparos
    # Si el disparo va a una casilla con barco del tablero del oponente, se imprime una X en el tablero a mostrar en pantalla       
    else:
        print("\nDisparo acertado!\n")
        time.sleep(0.75)
        tablero_disparos[fila][columna] = "X"
        print("Tablero contrincante: \n")
        print(tablero_disparos, "\n")
        print("\nVuelves a disparar...\n")
        time.sleep(0.75)
        disparar(jugador, tablero, tablero_disparos, fila, columna)

    return tablero_disparos

def jugar():
    '''
    La función importa las demás funciones creadas para el juego.
    Crea un sistema de turnos y cuando uno de los jugadores acierta a todos los barcos gana.
    '''
    from variables import lista_barcos
    from disparar import disparar
    from clases import Tablero
    import numpy as np
    import os
    import time 

    print("\nBienvenido al demo de hundir la flota!\n")
    input("Presiona cualquier tecla para continuar\n")
    os.system("cls")
    nombre_jugador = input("\nIntroduce tu nombre: ")
    time.sleep(0.75)
    print("\nAgregando barcos al tablero...")
    time.sleep(0.75)
    os.system("cls")
    # Crea un tablero de 10x10 vacío.
    jugador = Tablero(nombre_jugador, 0)
    tablero = jugador.crear_tablero()
    # Crea los barcos de la lista con una ubicación aleatoria.
    for barco in lista_barcos:
        jugador.crear_barco_random(barco[0], barco[1])
    # Le asigna el tablero con los barcos al jugador y luego lo imprime por pantalla al iniciar el juego.
    jugador_1 = tablero
    print("Barcos agregados aleatoriamente")
    print("\nTablero", nombre_jugador, "\n")
    print(jugador_1)
    # jugador_visible sera el tablero que vera el jugador por pantalla donde se muestren los disparos efectuados por el ordenador.
    jugador_visible = tablero
    # Se crea un tablero para el ordenador
    jugador = Tablero("Ordenador", 0)
    tablero = jugador.crear_tablero()
    # Se agregan los mismos barcos que para el jugador, en otro orden aleatorio.
    for barco in lista_barcos:
        jugador.crear_barco_random(barco[0], barco[1])
    # Se asigna a la variable ordenador el tablero creado con los barcos ubicados.
    ordenador = tablero
    # ordenador_visible es el tablero que ve el usuario con sus disparos efectuados, se imprime por pantalla al inciarse el juego.
    ordenador_visible = np.full((10, 10), " ", dtype=str)
    print("\nTablero ordenador\n")
    print(ordenador_visible)
    # Los contadores son los aciertos del oponente, contador_jugador es las veces que el oponente acerto.   
    contador_jugador = 0
    contador_ordenador = 0
    turno = 1
    presionar = input("\nPresione cualquier tecla para comenzar el juego\n")
    os.system("cls")
    # Mientras el contador no llegue al número que se indiquie en la demo, se sigue jugando.
    while contador_ordenador < 20 and contador_jugador < 20:
        # Para que los turnos vayan pasando de jugador a ordenador, se crea una variable turno que sera par e impar a medida que se recorre el bucle.
        if turno%2 != 0:
            # Turno jugador, se imprime el tablero del ordenador, se ejecuta la función disparar y luego se imprime el tablero
            # con los disparos efectuados y el número de aciertos hasta el momento.
            print("\nTurno jugador:")
            print("\nTablero ordenador:")
            print("\n", ordenador_visible, "\n")
            disparar(nombre_jugador, ordenador, ordenador_visible)
            time.sleep(0.75)
            os.system("cls")
            print("\nTablero", nombre_jugador, "\n")
            print(jugador_1)
            print("\nTablero ordenador:\n")
            print(ordenador_visible)
            cantidad_x = 0
            for i in ordenador_visible:
                x_por_fila = list(i).count('X')
                cantidad_x += x_por_fila 
            contador_ordenador = cantidad_x
            print("\nLlevas", contador_ordenador, "aciertos.")
            presionar = input("\nPresione la tecla 's' para salir del juego\nPresione cualquier otra tecla para que juege el ordenador: ")
            if presionar == "s" or presionar == "S":
                print("\nHasta luego,", nombre_jugador, "\n")
                os._exit(0)
            else:
                pass
            print("\nEsperando turno del ordenador...\n")
            time.sleep(1)
            os.system("cls") 

        elif turno%2 == 0:
            # Turno ordenador, se ejecuta la función disparar y luego se imprime el tablero del jugador
            # con los disparos efectuados y el número de aciertos hasta el momento.
            print("\nTurno ordenador:")
            time.sleep(0.75)
            disparar("ordenador", jugador_1, jugador_visible)
            time.sleep(0.75)
            print("Tablero", nombre_jugador, "\n")
            print(jugador_1, "\n")
            cantidad_x = 0
            for i in jugador_1:
                x_por_fila = list(i).count('X')
                cantidad_x += x_por_fila 
            contador_jugador = cantidad_x
            print("\nEl ordenador lleva", contador_jugador, "aciertos")
            presionar = input("\nPresione cualquier tecla para pasar a su turno\n")
            time.sleep(0.75)
            os.system("cls") 
        turno +=1
    else:
        if contador_jugador >= 20:
            print("-----------------------")
            print("Ha ganado el ordenador!")
            print("-----------------------")
        elif contador_ordenador >= 20:
            print("-----------------------")
            print("Has ganado,", nombre_jugador, "!")
            print("-----------------------")



