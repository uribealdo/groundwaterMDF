# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:10:40 2019

@author: gmb291
"""

import numpy as np
import matplotlib.pyplot as plt # combines namespace of numpy and pyplot

###SIMULACION DE AGUAS SUBTERRANEA
Lx=500
Ly=300

#Transmitivity
T=500 # m2/dia

nx=50
ny=30

dx=Lx/nx
dy=Ly/ny

x=np.zeros(nx+1)
y=np.zeros(ny+1)
x[0]=0
y[0]=0
for i in range(1,nx+1):
    x[i]=i*dx

for i in range(1,ny+1):
    y[i]=i*dy

s=(nx,ny)
h=np.zeros(s)
Q=np.zeros(s)
print(Q)
L=np.zeros(s)
ho=np.zeros(s)

#Condiciones de borde Q segun pozo
#Q[25,15]=2000
#Q[25,15]=2289
#Q[25,15]=2323
#Q[25,15]=2376
#Q[25,15]=2419
#Q[25,15]=2462
Q[25,15]=2505

#Condiciones de borde ho
L+=0.00002

#Proceso de itereacion

for k in range(1,1000):
    for i in range(1,nx-1):
        if i<nx-1:
            for j in range(0,ny):
                if j<1:
                    h[i][j]=((h[i][j+1]+h[i-1][j]+h[i+1][j])/(3+L[i][j]*dx**2/T)-(Q[i][j]-L[i][j]*ho[i][j]*dx**2)/(3*T+L[i][j]*dx**2))
                elif 1<j<ny-1:
                    h[i][j]=((h[i][j-1]+h[i][j+1]+h[i-1][j]+h[i+1][j])/(4+L[i][j]*dx**2/T)-(Q[i][j]-L[i][j]*ho[i][j]*dx**2)/(4*T+L[i][j]*dx**2))
                else:
                    h[i][j]=((h[i][j-1]+h[i-1][j]+h[i+1][j])/(3+L[i][j]*dx**2/T)-(Q[i][j]-L[i][j]*ho[i][j]*dx**2)/(3*T+L[i][j]*dx**2))
        else:
            i==nx
            for j in range(0,ny):
                if j<1:
                    h[i][j]=((h[i][j+1]+h[i-1][j])/(3+L[i][j]*dx**2/T)-(Q[i][j]-L[i][j]*ho[i][j]*dx**2)/(3*T+L[i][j]*dx**2))
                elif 1<j<ny-1:
                    h[i][j]=((h[i][j-1]+h[i][j+1]+h[i-1][j])/(4+L[i][j]*dx**2/T)-(Q[i][j]-L[i][j]*ho[i][j]*dx**2)/(4*T+L[i][j]*dx**2))
                else:
                    h[i][j]=((h[i][j-1]+h[i-1][j])/(3+L[i][j]*dx**2/T)-(Q[i][j]-L[i][j]*ho[i][j]*dx**2)/(3*T+L[i][j]*dx**2))
    
    ho=h        
np.savetxt('h_groundwater.dat', h, fmt='%.4e')

#Plotting##########
figura=plt.figure(1) 
plt.clf()
cs=plt.contour(h)
#plt.colorbar()
plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title("Superficie de nivel freatico")
plt.clabel(cs, inline=0.5, fontsize=8)
plt.savefig('D:/PYTHON/Groundwater/Contour.png', dpi=1800)

figura=plt.figure(2)
plt.contour(h)
plt.contourf(h,8,alpha=1,cmap='jet')
plt.colorbar()
plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title("Mapa de nivel freatico")
plt.savefig('D:/PYTHON/Groundwater/Mapping.png', dpi=1800)

# Guardar datos en archivo CSV

# Filtrado de Datos para el pozo
h_pozox=h[:,15]
h_pozoy=h[25,:]  

#Ploteo seccion X-X
figura=plt.figure(3) 
plt.clf()
plt.plot(h_pozox)
plt.xlabel('x [m]')
plt.ylabel('h [m]')
plt.title("Cross Section x-x")
plt.savefig('D:/PYTHON/Groundwater/section2d_x-x.png', dpi=1800)

#Ploteo seccion Y-Y
figura=plt.figure(4) 
fig=plt.plot(h_pozoy)
plt.xlabel('y [m]')
plt.ylabel('h [m]')
plt.title("Cross Section y-y")

plt.savefig('D:/PYTHON/Groundwater/section2d_y-y.png', dpi=1800)

