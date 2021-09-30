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

Clase Cromosoma

@author: asdruballopezchau
"""
import numpy as np
import random


class Cromosoma:
    def __init__(self,nbits=12, min=-1., max=1.):
        '''
        Crea un cromosoma con dos genes (x, y), cada uno
        de longitud nbits

        Parameters
        ----------
        nbits : int, optional
                DESCRIPTION. Número de bits en cada gen
        min: float, optional
                DESCRIPTION. Valor mínimo del intervalo
        max: float, optional
                DESCRIPTION. Valor máximo del intervalo
        Returns
        -------
        None.

        '''
        self.nbits = nbits
        x = random.choices([0, 1], k=nbits)
        y = random.choices([0, 1], k=nbits)
        self.cromosoma = [x, y]
        self.min = min
        self.max = max
        self.delta = np.abs(self.min - self.max)/np.power(2., nbits)
    
    def list2String(self, lista):
        return str(lista).replace("[","").replace("]","").replace(",","").replace(" ","")
    
    def toInt(self, lista):
        return int(self.list2String(lista), 2)
    
    def mutar(self):
        '''
        Mutación de un individuo
 
        Returns
        -------
        None.

        '''
        # Elige un índice aleatorio
        idx = random.choice(range(len(self.cromosoma[0])))
        # Cambia el bit del gen x
        self.cromosoma[0][idx] = 1 - self.cromosoma[0][idx]
        # Elige un índice aleatorio
        idx = random.choice(range(len(self.cromosoma[1])))
        # Cambia el bit del gen y        
        self.cromosoma[1][idx] = 1 - self.cromosoma[1][idx]
    
    def cruzar(self, madre):
        '''
        Cruza por un punto

        Parameters
        ----------
        madre : Cromosoma
            DESCRIPTION. Progenitor madre.

        Returns
        -------
        list
            DESCRIPTION. Hijos con genes de ambos progenitores.

        '''        
        hijo1 = Cromosoma()
        hijo2 = Cromosoma()
        hijo1.cromosoma[0] = self.cromosoma[0].copy()
        hijo1.cromosoma[1] = madre.cromosoma[1].copy()
        
        hijo2.cromosoma[0] = madre.cromosoma[0].copy()
        hijo2.cromosoma[1] = self.cromosoma[1].copy()
        return [hijo1, hijo2]
    
    def fenotipo(self):
        '''
        Obtiene los valores que representa el individuo

        Returns
        -------
        list
            valor real de x, y

        '''        
        particionX = self.toInt(self.cromosoma[0])
        particionY = self.toInt(self.cromosoma[1])
        xreal = self.min + self.delta*particionX
        yreal = self.min + self.delta*particionY
        return [xreal, yreal]

    def __str__(self):
        return str(self.cromosoma)