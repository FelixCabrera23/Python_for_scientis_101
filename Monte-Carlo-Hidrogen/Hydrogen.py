#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atomo de hidrogeno 1
Created on Fri Aug 30 10:57:42 2024

@author: pdam-linux
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constantes
a0 = 1  # Radio de Bohr, en unidades atómicas

# Número de simulaciones
num_simulaciones = 10000

# Generar posiciones aleatorias utilizando la distribución de probabilidad
# Muestreo de r
r = np.random.exponential(scale=a0, size=num_simulaciones)

# Muestreo de theta (uniforme en [0, pi])
theta = np.arccos(1 - 2 * np.random.rand(num_simulaciones))

# Muestreo de phi (uniforme en [0, 2pi])
phi = 2 * np.pi * np.random.rand(num_simulaciones)

# Convertir coordenadas esféricas a cartesianas
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Visualizar en un gráfico 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='blue', s=1, alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Distribución de posiciones del electrón en un átomo de hidrógeno')

plt.show()