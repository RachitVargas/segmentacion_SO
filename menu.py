#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:33:11 2021

@author: antony.vargasulead.ac.cr
"""


class Menu():

  def __init__(self, n_instrucciones, segmentacion):
    self.__n_instrucciones = n_instrucciones
    self.__segmentacion = segmentacion

  @property
  def n_instrucciones(self):
    return self.__n_instrucciones
  
  @property
  def segmentacion(self):
    return self.__segmentacion
  
  @n_instrucciones.setter
  def n_instrucciones(self, n_instrucciones):
    self.__n_instrucciones = n_instrucciones
  
  @segmentacion.setter
  def segmentacion(self, segmentacion):
    self.__segmentacion = segmentacion

  def __str__(self):
    return 'N. Instrucciones: ' + str(self.__n_instrucciones) +\
    '\nSegmentacion: ' + str(self.__segmentacion)