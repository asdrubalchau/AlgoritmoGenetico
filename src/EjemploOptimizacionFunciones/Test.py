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

Clase AlgEvolutivo
@author: asdruballopezchau
"""

from AlgEvolutivo import AlgEvolutivo
from FuncionAptitud import FuncionAptitud
from Cromosoma import Cromosoma
from Seleccion import Seleccion

class TestAE:
    def __init__(self, N, G):
        '''
        

        Parameters
        ----------
        N : int
            Tamaño población
        G : Int
            Número de generaciones

        Returns
        -------
        None.

        '''        
        self.N = N
        self.G = G
        
    def test(self):
        fitnessFunc = FuncionAptitud() 
        mecSel = Seleccion(fitnessFunc)
        poblacion = []
        for i in range(N):
            poblacion.append(Cromosoma())
        
        ae = AlgEvolutivo(poblacion, fitnessFunc, mecSel, self.N)
        ae.evolve(self.G,  showAll=False, showBest=False)
        print("Tamaño población:", self.N)
        print("Generaciones:", self.G)
        print(ae.best())
        print(ae.best().fenotipo())
        print(fitnessFunc.aptitud(ae.best()))
N = 200
G = 10
test = TestAE(N, G)
test.test()


