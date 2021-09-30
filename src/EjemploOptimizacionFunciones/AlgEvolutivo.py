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

import random
import numpy as np

class AlgEvolutivo:
      
    
    def __init__(self, poblacion, fitnessFunction, mecanismoSeleccion, N=100):
        self.fitnessFunction = fitnessFunction
        self.mecanismoSeleccion = mecanismoSeleccion
        self.N = N
        self.counterGenerations = 0
        self.poblacion = poblacion

    def elitismo(self, hijos=None):
        '''
        Returns
        -------
        mejor : Cromosoma
            DESCRIPTION. Una copia del mejor individuo 

        '''
        if hijos is None:
            todos = self.poblacion
        else:
            todos = self.poblacion.copy()
            todos.extend(hijos)
        return self.mecanismoSeleccion.elitismo(todos)
        
    
    def elegirSiguienteGeneracion(self,padres, hijos):
        todos = padres.copy()
        todos.extend(hijos)
        siguiente = self.mecanismoSeleccion.seleciona(todos, self.N)
        return siguiente
        
    
    def aptitudPoblacion(self):
        '''
        Calcula la aptitud de cada individuo en la población

        Returns
        -------
        aptitudes : List
            DESCRIPTION. Aptitudes de cada individuo

        '''
        
        aptitudes = []
        for individuo in self.poblacion:
            aptitudes.append(self.fitnessFunction.aptitud(individuo))
        return aptitudes
        
        
    def cruzar(self):
        '''
        Cruza individuos para crear nuevos

        Returns
        -------
        descendencia : List
            DESCRIPTION. Hijos

        '''
        # Elegir padres/madres
        K = int(len(self.poblacion)/2)
        padres = self.mecanismoSeleccion.seleciona(self.poblacion, K)
        madres = self.mecanismoSeleccion.seleciona(self.poblacion, K)
        descendencia = []
        for mama, papa in zip(madres, padres):
                hijo, hija = mama.cruzar(papa)
                descendencia.append(hija)
                descendencia.append(hijo)
        return descendencia    
        
    def mutar(self, mutables, porcentaje=0.05):
        '''
        Aplica mutación a los elementos de una lista de individuos (Cromosoma)

        Parameters
        ----------
        mutables : List
            DESCRIPTION. Contiene objetos Cromosoma
        porcentaje : TYPE, optional
            DESCRIPTION. Porcentaje de mutación, predeterminado 5%

        Returns
        -------
        mutables : TYPE
            DESCRIPTION.

        '''
        if porcentaje > 1:
            porcentaje = 1.
        totalMutar = np.ceil(len(mutables) * porcentaje)
         # Muta a algunos individuos seleccionados estocásticamente.
        for i in range(int(totalMutar)):
                idx = random.randrange(0, len(mutables))
                mutables[idx].mutar()         
        return mutables
    
    def poblacion2str(self, fenotipo=True):
        
        
        '''
        Regresa una cadena representando a toda la población

        Parameters
        ----------
        aptitudes : List
            Las aptitudes de los individuos
        fenotype : Boolean, optional
            DESCRIPTION. True se usan valores reales, False se usan genotipos.
        Returns
        -------
        cad : str
            DESCRIPTION. Cadena de la población con aptitudes

        '''
        cad = ""
        aptitudes = self.aptitudPoblacion()
        for ind, aptitud in zip(self.poblacion, aptitudes):
            if fenotipo:
                cad + str(ind.fenotipo()) + " FITNESS =  " + str(aptitud) + "\n"        
            else:
                cad = cad + str(ind) + " FITNESS =  " + str(aptitud) + "\n"        
            
        return cad

    def evolve(self,steps=1, showAll=False, showBest=True, showPhenotype=True):
        for i in range(steps):
            hijos = self.cruzar()
            mutados = self.mutar(hijos)            
            mejorSolucion = self.elitismo(mutados)
            siguientePoblacion = self.elegirSiguienteGeneracion(self.poblacion, hijos)
            siguientePoblacion.append(mejorSolucion)
            self.mejorSolucion = mejorSolucion
            self.poblacion = siguientePoblacion
            
            if showAll:
                print("\nGeneración: " + str(i))
                print(self.poblacion2str(showPhenotype))
            if showBest:
                if showPhenotype:
                    ind = str(mejorSolucion.fenotipo())
                else:
                    ind = str(mejorSolucion)
                mejorAptitud = self.fitnessFunction.aptitud(mejorSolucion)
                print("El mejor de la generación ")
                print("Individuo: " +str(ind) + " Aptitud: "+ str(mejorAptitud))
        
    def best(self):
        return self.mejorSolucion
    
            
        
        
        