#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Genéticos
Tema: Optimización de funciones
Profesor: Dr. Asdrúbal López Chau

Descripción: Ejemplo de función multimodal univariada

@author: asdruballopezchau

"""
from matplotlib import pyplot as plt
import numpy as np

def f1(x):
    return np.sin(x)*np.cos(3*x)

x = np.linspace(-5, 5, 100)
fx = f1(x)
plt.plot(x, fx) 
plt.xlabel("x")
plt.ylabel("f1(x)")
plt.title("f1(x)=sin(x)*cos(3x)")
plt.grid()

