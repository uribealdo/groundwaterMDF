# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:14:24 2019

@author: uribe
"""
# Importar librerias
import pandas as pd
import matplotlib.pyplot as plt #plt es el nombre de la variable

data=pd.ExcelFile('Data_pozo.xlsx')
print(data.sheet_names)

#Importar Data Descenso
Desc=data.parse('Descenso')
#print(Desc)
td=Desc['Tiempo']
#print(td)
zd=Desc['Nivel']
#print(zd)
#Importar Data Ascenso
Asc=data.parse('Ascenso')
#print(Asc)
ta=Asc['Tiempo']
#print(ta)
za=Asc['Nivel']
#print(za)


# Ploteo de Datos
plt.clf()
plt.subplot(2,1,1)
plt.plot(td,zd)
plt.xlabel('t(s)')
plt.ylabel('z (m)')
plt.legend(['Descenso'])
plt.show()

# Ploteo de Datos
plt.subplot(2,1,2)
plt.plot(ta,za)
plt.xlabel('t(s)')
plt.ylabel('z (m)')
plt.legend(['Ascenso'])
plt.show()