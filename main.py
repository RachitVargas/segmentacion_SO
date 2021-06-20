#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:08:40 2021

@author: antony.vargasulead.ac.cr
"""

import numpy as np
from procesador import Procesador
from interfaz import Interfaz
from menu import Menu


def main():
    
    an_interfaz = Interfaz
    eleccion = 0
    
    while eleccion != 2:
        
        print('[Bienvenido al simulador]')
        print('Por favor elija: \n1. Correr simulacion \n2. Salir de la simulacion:')
        eleccion = int(input())
        
        if eleccion == 1:
            
            n_instrucciones = an_interfaz.n_instrucciones()
            tipo_segmentacion = an_interfaz.segmentacion()
            menu = Menu(n_instrucciones, tipo_segmentacion)

            procesador = Procesador(menu)
            print('Resultado de ' + str(n_instrucciones) +\
                  ' instrucciones con el tipo ' + str(tipo_segmentacion) + ' es: ' +\
                      str(procesador.resultado) + ' ciclos de reloj')
                
        elif eleccion == 2:
            print('Muchas gracias')
            
        else:
            print('Ops, ha ocurrido un problema.')

if __name__ == '__main__':
    main()
    
    
    
    
    
    