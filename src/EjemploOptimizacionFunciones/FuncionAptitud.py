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

Clase Función aptitud


@author: asdruballopezchau
"""
import numpy as np
from Cromosoma import Cromosoma

class FuncionAptitud:
    
    def f(self, x,y):
        return (np.sin(x)*np.cos(3*y))*np.sin(5*x)

    def aptitud(self, cromosoma):
        '''
        Función para evaluar la aptitud del individuo

        Parameters
        ----------
        cromosoma : Cromosoma
            Individuo a evaluar

        Returns
        -------
        float
            Aptitud del individuo

        '''
        x, y = cromosoma.fenotipo()
        return -self.f(x, y)
    
        