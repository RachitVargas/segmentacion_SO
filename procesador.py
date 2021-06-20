#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:37:46 2021

@author: antony.vargasulead.ac.cr
"""
import numpy as np

class Procesador():
  
  def __init__(self, menu):
    self.__menu = menu
    self.__n_instrucciones = self.__menu.n_instrucciones
    self.__segmentacion = self.__menu.segmentacion
    self.__resultado = self.__modelo(self.__n_instrucciones, self.__segmentacion)
  
  @property
  def menu(self):
    return print(self.__menu)

  @menu.setter
  def menu(self, menu):
    self.__menu = menu

  @property
  def n_instrucciones(self):
    return self.__n_instrucciones
  
  @property
  def segmentacion(self):
    return self.__segmentacion

  def __fetch(self):
      tiempo_fetch = 5
      return tiempo_fetch

  def __acceso_memoria(self):
      tiempo_memoria = np.random.randint(10, 21)
      return tiempo_memoria
  
  def __ejecucion(self):
      tiempo_ejecucion = np.random.randint(10, 46)
      return tiempo_ejecucion
  
  def __retroestricta(self):
      tiempo_retro = np.random.randint(10,21)
      return tiempo_retro
  
  def act_procesador(self):
      tiempo_actualizacion = 10
      return tiempo_actualizacion
    
  def __proceso_sin_segmentacion(self, n_instrucciones):
    cola = []

  def __proceso_segmentacion(self, n_instrucciones):
    cola = []
  
  def __modelo(self, n_instrucciones, segmentacion):
      
      resultado = 0
      if segmentacion == 2:
          resultado = self.__proceso_segmentacion(n_instrucciones)
      else:
          resultado = self.__proceso_sin_segmentacion(n_instrucciones)
      
      return resultado
