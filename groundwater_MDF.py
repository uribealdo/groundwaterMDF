# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:10:40 2019

@author: gmb291
"""

import numpy as np
Lx=5000
Ly=3000

#Transmitivity
T=500 # m2/dia

nx=50
ny=20

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
#Q[20,10]=1000
Q[10,15]=2000
#Q[30,5]=2000
#Q[40,5]=2000
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

import matplotlib.pyplot as plt # combines namespace of numpy and pyplot

plt.clf()
plt.subplot(2,2,1)
cs=plt.contour(h)
#plt.colorbar()
plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title("Curvas")
plt.clabel(cs, inline=0.5, fontsize=8)

plt.subplot(2,2,2)
plt.contour(h)
plt.contourf(h,8,alpha=1,cmap='jet')
plt.colorbar()
plt.xlabel('y [m]')
#plt.ylabel('x [m]')
plt.title("Curvas")

plt.savefig('E:/A.-TESIS_MAESTRÍA/CICLO 2019-I/TE-Groundwater/imagen.png', dpi=1800)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(nx,ny,h,cmap='jet')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')