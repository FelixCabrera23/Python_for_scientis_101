#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:58:29 2024

@author: pdam-linux
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constantes
Z = 2  # Carga nuclear del helio
a0 = 1  # Radio de Bohr en unidades atómicas
e2_4pi_epsilon0 = 1  # Constante para simplificar la notación

# Número de simulaciones
num_simulaciones = 10000
delta = 0.5  # Tamaño del paso para las propuestas

# Función para calcular la energía de la configuración
def energia_total(r1, r2):
    r1_norm = np.linalg.norm(r1)
    r2_norm = np.linalg.norm(r2)
    r12_norm = np.linalg.norm(r1 - r2)
    
    energia = (-Z * e2_4pi_epsilon0 / r1_norm) + (-Z * e2_4pi_epsilon0 / r2_norm) + (e2_4pi_epsilon0 / r12_norm)
    return energia

# Inicialización de las posiciones de los electrones
r1 = np.random.uniform(-a0, a0, 3)
r2 = np.random.uniform(-a0, a0, 3)

# Lista para guardar las posiciones aceptadas
posiciones_r1 = []
posiciones_r2 = []

# Algoritmo de Montecarlo
for _ in range(num_simulaciones):
    # Calcular la energía actual
    energia_actual = energia_total(r1, r2)
    
    # Proponer un nuevo movimiento para r1
    r1_nuevo = r1 + np.random.uniform(-delta, delta, 3)
    
    # Calcular la energía de la nueva configuración
    energia_nueva = energia_total(r1_nuevo, r2)
    
    # Criterio de Metropolis
    if np.random.rand() < np.exp(-(energia_nueva - energia_actual)):
        r1 = r1_nuevo  # Aceptar la nueva posición
    
    # Guardar las posiciones aceptadas
    posiciones_r1.append(r1)
    posiciones_r2.append(r2)
    
    # Proponer un nuevo movimiento para r2
    r2_nuevo = r2 + np.random.uniform(-delta, delta, 3)
    
    # Calcular la energía de la nueva configuración
    energia_nueva = energia_total(r1, r2_nuevo)
    
    # Criterio de Metropolis
    if np.random.rand() < np.exp(-(energia_nueva - energia_actual)):
        r2 = r2_nuevo  # Aceptar la nueva posición
    
    # Guardar las posiciones aceptadas
    posiciones_r1.append(r1)
    posiciones_r2.append(r2)

# Convertir listas a arrays para facilitar el manejo
posiciones_r1 = np.array(posiciones_r1)
posiciones_r2 = np.array(posiciones_r2)

# Visualizar en un gráfico 3D
fig = plt.figure(figsize=(12, 6))

# Electrón 1
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(posiciones_r1[:, 0], posiciones_r1[:, 1], posiciones_r1[:, 2], c='blue', s=1, alpha=0.5)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Distribución de posiciones del electrón 1')

# Electrón 2
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(posiciones_r2[:, 0], posiciones_r2[:, 1], posiciones_r2[:, 2], c='red', s=1, alpha=0.5)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Distribución de posiciones del electrón 2')

plt.show()