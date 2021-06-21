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

  @property
  def resultado(self):
      return self.__resultado

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
  
  def __act_procesador(self):
      tiempo_actualizacion = 10
      return tiempo_actualizacion
    
  def __proceso_sin_segmentacion(self, n_instrucciones):
      cola = []
      bloques = 5
      tiempo_total = 0
      for i in range(n_instrucciones):
          cola.append(self.__fetch())
          cola.append(self.__acceso_memoria())
          cola.append(self.__ejecucion())
          cola.append(self.__retroestricta())
          cola.append(self.__act_procesador())
          for j in range(bloques):
              tiempo_total += cola.pop(0)
      print(tiempo_total)
      return (tiempo_total / (n_instrucciones))
        
  def __proceso_segmentacion(self, n_instrucciones):
      tiempo_total = 0
      memoria = []
      
      unidad_1 = []
      unidad_2 = []
      unidad_3 = []      
      
      for i in range(n_instrucciones):
          memoria.append(self.__fetch())
          memoria.append(self.__acceso_memoria())
          memoria.append(self.__ejecucion())
          memoria.append(self.__retroestricta())
          memoria.append(self.__act_procesador())
     
      controlador = 1
      while len(memoria) != 0:
          if controlador == 1:
              unidad_1.append(memoria.pop(0))
              controlador = 2
          elif controlador == 2:
              unidad_2.append(memoria.pop(0))
              controlador = 3
          elif controlador == 3:
              unidad_3.append(memoria.pop(0))
              controlador = 1
      tiempo_total = ((sum(unidad_1) + sum(unidad_2) + sum(unidad_3))/3)
      return (tiempo_total / (n_instrucciones))
      
         
  def __modelo(self, n_instrucciones, segmentacion):
      
      resultado = 0
      if segmentacion == 1:
          resultado = self.__proceso_segmentacion(n_instrucciones)
      elif segmentacion == 2:
          resultado = self.__proceso_sin_segmentacion(n_instrucciones)
      else:
          print('Ops, ocurrio algun error antes de correr la simunacion.')
        
      return resultado
