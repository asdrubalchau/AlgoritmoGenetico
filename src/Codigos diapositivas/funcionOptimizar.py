#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Genéticos
Tema: Optimización de funciones
Profesor: Dr. Asdrúbal López Chau

Descripción: Gráfica de función a optimizar
f(x,y) = (sin(x)*cos(3y))*sin(5x)
@author: asdruballopezchau

"""
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def f(x, y):
    return (np.sin(x)*np.cos(3*y))*np.sin(5*x)

b = np.arange(-1., 1., 0.1)
d = np.arange(-1., 1., 0.1)

X, Y = np.meshgrid(b, d)
fxy = f(X, Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, fxy)
plt.xlabel('x')
plt.ylabel('y')
plt.zlabel('f(x,y)')
plt.show()