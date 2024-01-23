from variables import dim
import pandas as pd
import numpy as np
import random

class Tablero:
    
    def __init__(self, id_jugador:str, barcos=0):
        '''
        Crea un objeto de la clase tablero.
        id_jugador: nombre del jugador al que pertenece el tablero.
        barcos: cantidad de barcos, por defecto cero.
        '''
        self.id_jugador = id_jugador
        self.barcos = barcos

    def crear_tablero(self):
        '''
        Crea un tablero de dimensión 10x10
        '''
       
        self.tablero = np.full(dim, " ", dtype=str)
        return self.tablero

    def crear_barco_random(self, eslora:int, inicial:str):
        '''
        Ubica un barco en una ubicación aleatoria, dada una posición inicial y la cantidad de casillas que ocupa el barco.
        El sentido(Norte, Sur, etc...) se da de manera aleatoria, la función primero intenta ubicar la casilla inicial, que
        debe estar vacía, luego crear el barco según sus dimensiones y el sentido que tocó, si esto no es posible intenta
        con el próximo sentido. Si no es posible ubicar el barco en ninguno de los 4 sentidos, escoge otra casilla inicial
        aleatoria y lo vuelve a intentar, así hasta conseguir ubicar el barco.
        '''
        
        # Ubicación inicial aleatoria
        i = random.randint(0,9)
        j = random.randint(0,9)
        # Orientación aleatoria
        orientacion = random.randint(1,4)
        try:
            # Si la posición inicial está ocupada, vuelve a intentar
            if self.tablero[i][j] == " ":
                # El bucle intenta ubicar el barco por cada una de las orientaciones posibles.
                contador = 0
                while contador < 4:
                    if orientacion == 1:
                        barco_random = []
                        for k in range(eslora):
                            # Crea el barco casilla a casilla
                            barco_random.append((i-k, j))
                        # Comprueba que el barco no se salga del rango
                        if 0 <= ((barco_random[0][0])-(eslora-1)) <= 9:
                            # Comprueba que las casillas del barco creado no coincidan con uno existente.
                            coincidencias = 0
                            for casilla in barco_random:
                                if self.tablero[casilla[0]][casilla[1]] != " ":
                                    coincidencias +=1
                            # Si no hay coincidencias se crea el barco
                            if coincidencias == 0:
                                for casilla in barco_random:
                                    self.tablero[casilla[0]][casilla[1]] = inicial
                                return self.tablero
                            # Si hay coincidencias, pasa para que continue el bucle while e intente con otra orientacion.
                            else:
                                pass             
                        else:
                            pass
                    elif orientacion == 2:
                        barco_random = []
                        for k in range(eslora):
                            barco_random.append((i+k, j))                       
                        if 0 <= ((barco_random[0][0])+(eslora-1)) <= 9:
                            coincidencias = 0
                            for casilla in barco_random:
                                if self.tablero[casilla[0]][casilla[1]] != " ":
                                    coincidencias +=1
                            if coincidencias == 0:
                                for casilla in barco_random:
                                    self.tablero[casilla[0]][casilla[1]] = inicial
                                return self.tablero
                            else:
                                pass
                        else:
                            pass
                    elif orientacion == 3:
                        barco_random = []
                        for k in range(eslora):
                            barco_random.append((i, j+k))                       
                        if 0 <= ((barco_random[0][1])+(eslora-1)) <= 9:
                            coincidencias = 0
                            for casilla in barco_random:
                                if self.tablero[casilla[0]][casilla[1]] != " ":
                                    coincidencias +=1
                            if coincidencias == 0:
                                for casilla in barco_random:
                                    self.tablero[casilla[0]][casilla[1]] = inicial
                                return self.tablero
                            else:
                                pass
                        else:
                            pass
                    elif orientacion == 4:
                        barco_random = []
                        for k in range(eslora):
                            barco_random.append((i, j-k))                        
                        if 0 <= ((barco_random[0][1])-(eslora-1)) <= 9:
                            coincidencias = 0
                            for casilla in barco_random:
                                if self.tablero[casilla[0]][casilla[1]] != " ":
                                    coincidencias +=1
                            if coincidencias == 0:
                                for casilla in barco_random:
                                    self.tablero[casilla[0]][casilla[1]] = inicial
                                return self.tablero
                            # Vuelve a definir orientación como 0 para que al sumar intente en la orientación Norte.
                            else:
                                orientacion = 0
                        else:
                            orientacion = 0 
                    # Suma 1 a orientación, en la siguiente ejecución del bucle intenta con la proxima orientación    
                    orientacion += 1
                    # Se agrega uno a contador, al llegar a 4 deja de ejecutarse el bucle ya que se probó con las 4 orientaciones posibles.                     
                    contador += 1 
                # Devuelve el tablero con las casillas impresas.
                return self.crear_barco_random(eslora, inicial)
            else:
                return self.crear_barco_random(eslora, inicial)
        # Si no se ejecuta el try, quiere decir que ya no hay casillas disponibles para crear el barco requerido.
        except:
            print("Ya no quedan espacios disponibles para agregar un barco de dimension", eslora)