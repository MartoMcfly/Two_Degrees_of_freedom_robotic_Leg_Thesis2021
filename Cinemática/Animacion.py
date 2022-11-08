#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue JJun  21 16:56:00 2021

@author: Jaime Nunez
"""

import numpy as np
import Trayectoria as TR
from tabulate import tabulate
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from Cinematica import Cinematica_Directa


#Parametros geometricos
L1, L2=1,1 
def make_plot(i,X,Y):
    # Plot y guardar la imagen
    ax.plot([0, X[0][i], X[1][i]], [0, Y[0][i], Y[1][i]], lw=2, c='k')
    
    # Circulo: Representacion movimiento rotacional
    r=0.05
    c0 = Circle((0, 0), r/2, fc='k', zorder=10)
    c1 = Circle((X[0][i], Y[0][i]), r, fc='b', ec='b', zorder=10)
    c2 = Circle((X[1][i], Y[1][i]), r, fc='r', ec='r', zorder=10)
    ax.add_patch(c0)
    ax.add_patch(c1)
    ax.add_patch(c2)

    # Centre the image on the fixed anchor point, and ensure the axes are equal
    ax.set_xlim(-L1-L2-r, L1+L2+r)
    ax.set_ylim(-L1-L2-r, L1+L2+r)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig('frames/_img{:04d}.png'.format(i//di), dpi=72)
    plt.cla()

#Tiempo de Muestreo
dt=0.1
tf=2
t=np.arange(0,tf+dt,dt)

#Trayectoria Articular
Theta1=TR.Trayectoria(np.deg2rad(210), np.deg2rad(-70), t, tf)
Theta2=TR.Trayectoria(np.deg2rad(115), np.deg2rad(-15), t, tf)
Theta=np.array([Theta1,Theta2])

#Parametros Denavit Hartenberg
Vars=0
GL=2
DoF=[]
for i in range (1,GL+1):
    V=i
    DoF.append(V)

a1=1
a2=1
a=[a1,a2]

d1=1
d2=1
d=[d1,d2]

Alfa1=np.pi
Alfa2=np.pi
Alfa=[Alfa1,Alfa2]

#Tabla de Parametros
Tabla=[['DoF','a','d','Alfa'],[DoF,a,d,Alfa]]
print(tabulate(Tabla, headers='firstrow', tablefmt='fancy_grid'))

#Posicion Final: Coordenadas Operacionales
DatosX=Cinematica_Directa(a, d, Alfa, Theta, t,Vars)[0]
DatosY=Cinematica_Directa(a, d, Alfa, Theta, t,Vars)[1]
DatosZ=Cinematica_Directa(a, d, Alfa, Theta, t,Vars)[2]  

#Grafica Posicion Operacional: Cada Eslabon
plt.plot(t,DatosX[1])
plt.plot(t,DatosY[1])
plt.show()

# Hacer la imagen para cada di de tiempo
# frames per second.
# Frame rate, s-1
fps = 10
di = int(1/fps/dt)
fig = plt.figure(figsize=(8.3333, 6.25), dpi=72)
ax = fig.add_subplot(111)

for i in range(0, t.size, di):
    print(i // di, '/', t.size // di)
    make_plot(i,DatosX,DatosY)
