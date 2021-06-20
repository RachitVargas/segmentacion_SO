#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:56:55 2021

@author: antony.vargasulead.ac.cr
"""

class Interfaz():
    
    def n_instrucciones():
        print('Seleccione la cantidad de instrucciones:')
        print('1. 1000 \n2. 5000 \n3. 10000')
        
        eleccion = int(input())
        cantindad_instrucciones = 0
        if eleccion == 1:
            cantindad_instrucciones = 1000
        elif  eleccion == 2:
            cantindad_instrucciones = 5000
        else:
            cantindad_instrucciones = 10000
        
        return cantindad_instrucciones
        
    def segmentacion():
        print('Elija el tipo de segmentacion:')
        print('1. Con Segmentacion \n2. Sin Segmentacion')
        eleccion = int(input())

        return eleccion