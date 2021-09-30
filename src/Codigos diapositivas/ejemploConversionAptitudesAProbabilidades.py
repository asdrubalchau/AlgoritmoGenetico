#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Genéticos
Tema: Optimización de funciones
Profesor: Dr. Asdrúbal López Chau

Descripción: Ejemplo de como convertir a probabilidades las aptitudes de los
individuos para optimizar la función
f(x,y) = (sin(x)*cos(3y))*sin(5x)

@author: asdruballopezchau
"""
import numpy as np

def f(x, y):
    return (np.sin(x)*np.cos(3*y))*np.sin(5*x)
# Genera algunos valores de x, y en el intervalor (-1, 1]
x = 2*np.random.random(5)-1
y = 2*np.random.random(5)-1
# La aptitud propuesta es -f(x, y), como se explica en las diapositivas
fi = -f(x, y)
# Ajuste de aptitudes
fiprima = (fi + abs(min(fi))) / max((fi + abs(min(fi))))
# Uso de la función softmax para convertir en probabilidades
probabilidades = np.exp(fiprima) / np.sum(np.exp(fiprima))
