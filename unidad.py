#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:36:23 2021

@author: antony.vargasulead.ac.cr
"""

class Unidad():

    def __init__(self, disponible):
        self.__unidad_disponible = disponible
        self.__cola = []

    @property
    def unidad_disponible(self):
        return self.__unidad_disponible
    
    @unidad_disponible.setter 
    def unidad_disponible(self, unidad_disponible):
        self.__unidad_disponible = unidad_disponible
        
    @property
    def cola(self):
        return self.__cola
    
    @cola.setter
    def cola(self, valor):
        self.__cola.append(valor)