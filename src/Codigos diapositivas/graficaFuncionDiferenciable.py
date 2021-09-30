#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Genéticos
Tema: Optimización de funciones
Profesor: Dr. Asdrúbal López Chau

Descripción: Ejemplo: Se necesita una superficie 
rectangular cercada por tres lados con tela metálica 
y por el cuarto lado con un muro de piedra. 
Se dispone de 20 metros lineales de tela metálica. 
Calcula las dimensiones queha de tener  la 
superficie para que su área sea la mayor posible. 
Ejemplo de https://www.ecured.cu/Optimizaci%C3%B3n_de_funciones

@author: asdruballopezchau
"""

from matplotlib import pyplot as plt
import numpy as np
def A(x):
     return 20*x - 2*np.power(x, 2.0)
 
x = np.linspace(0, 10, 100)
fx = A(x)
plt.plot(x, fx) 
plt.xlabel("x")
plt.ylabel("Area")
plt.grid()
    
 