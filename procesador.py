#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:37:46 2021

@author: antony.vargasulead.ac.cr
"""

from menu import Menu

class Procesador():
  
  def __init__(self, menu):
    self.__menu = menu
    self.__n_instrucciones = self.__menu.n_instrucciones
    self.__segmentacion = self.__menu.segmentacion

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

  def __proceso_sin_segmentacion(self):
    pass

  def __proceso_segmentacion(self):
    pass