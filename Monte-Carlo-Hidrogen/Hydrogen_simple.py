import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constantes
a0 = 1  # Radio de Bohr en unidades atómicas
Z_efectiva = 1.5  # Carga efectiva aproximada para el helio

# Número de simulaciones
num_simulaciones = 10000

# Generar posiciones aleatorias para el primer electrón
r1 = np.random.exponential(scale=a0/Z_efectiva, size=num_simulaciones)
theta1 = np.arccos(1 - 2 * np.random.rand(num_simulaciones))
phi1 = 2 * np.pi * np.random.rand(num_simulaciones)

# Convertir coordenadas esféricas a cartesianas para el primer electrón
x1 = r1 * np.sin(theta1) * np.cos(phi1)
y1 = r1 * np.sin(theta1) * np.sin(phi1)
z1 = r1 * np.cos(theta1)

# Generar posiciones aleatorias para el segundo electrón (independiente)
r2 = np.random.exponential(scale=a0/Z_efectiva, size=num_simulaciones)
theta2 = np.arccos(1 - 2 * np.random.rand(num_simulaciones))
phi2 = 2 * np.pi * np.random.rand(num_simulaciones)

# Convertir coordenadas esféricas a cartesianas para el segundo electrón
x2 = r2 * np.sin(theta2) * np.cos(phi2)
y2 = r2 * np.sin(theta2) * np.sin(phi2)
z2 = r2 * np.cos(theta2)

# Visualizar en un gráfico 3D
fig = plt.figure(figsize=(8, 8))

# Electrón 1
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(x1, y1, z1, c='blue', s=1, alpha=0.5)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Distribución de posiciones del electrón 1')

# Electrón 2
#ax2 = fig.add_subplot(122, projection='3d')
ax1.scatter(x2, y2, z2, c='red', s=1, alpha=0.5)
#ax1.set_xlabel('X')
#ax1.set_ylabel('Y')
#ax1.set_zlabel('Z')
#ax2.set_title('Distribución de posiciones del electrón 2')

plt.show()