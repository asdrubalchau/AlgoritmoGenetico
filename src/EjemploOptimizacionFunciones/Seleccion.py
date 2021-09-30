#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Genéticos
Tema: Optimización de funciones
Profesor: Dr. Asdrúbal López Chau

Descripción: Optimizar la función
f(x,y) = (sin(x)*cos(3y))*sin(5x)

Clase Mecanismo Selección

@author: asdruballopezchau
"""

import numpy as np
from Cromosoma import Cromosoma
from FuncionAptitud import FuncionAptitud
import random

class Seleccion:
    
    def __init__(self, funcionAptitud):
        self.funcionAptitud = funcionAptitud
    
    def elitismo(self, poblacion):
        '''
        Selecciona el mejor individuo de una población,
        lo clona y lo regresa.

        Parameters
        ----------
        poblacion : List
            Contiene los individuos de una población

        Returns
        -------
        elite : Cromosoma
            Mejor individuo

        '''
        fi = self.calculaAptitudes(poblacion)
        fiprima = self.ajustaAptitudes(fi)
        idx = np.argmax(fiprima)
        elite = Cromosoma(poblacion[0].nbits)
        elite.cromosoma = poblacion[idx].cromosoma.copy()
        return elite
    
    def seleciona(self, poblacion, K):
        '''
        Selecciona K individuos de una población considerando
        la aptitud

        Parameters
        ----------
        poblacion : List
            Contiene los individuos de una población
        K : Int
            Número de individuos a elegir.

        Returns
        -------
        elegidos : list
            Individuos seleccionados (copia)

        '''
        
        
        fi = self.calculaAptitudes(poblacion)
        fiprima = self.ajustaAptitudes(fi)
        probabilidades = self.aptitudesAProbabilidades(fiprima)
        elegidos = random.choices(poblacion, 
                                  weights=probabilidades, 
                                  k=K).copy()
        return elegidos
        
    def calculaAptitudes(self, poblacion):
        fi = []
        for ind in poblacion:
            fi.append(self.funcionAptitud.aptitud(ind))
        return fi
    
    def ajustaAptitudes(self, fi):
        fi = np.array(fi)
        # Ajuste de aptitudes
        fiprima = (fi + abs(min(fi))) / max((fi + abs(min(fi))))
        return fiprima
    
    def aptitudesAProbabilidades(self, fiprima):
        # Uso de la función softmax para convertir en probabilidades
        probabilidades = np.exp(fiprima) / np.sum(np.exp(fiprima))
        return probabilidades