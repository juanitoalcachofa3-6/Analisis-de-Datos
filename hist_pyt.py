import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

 #Lectura del archivo
df=pd.read_csv('/home/danykruger/Descargas/WhatsApp/juanito/doptimalidad/organizador3/datos_filtrados_semana_1.csv')

T=df['T'].dropna()

#Línea de densidad
dens=gaussian_kde(T)
val_x=np.linspace(T.min(),T.max(),500)
val_y=dens(val_x)

#histograma
plt.hist(T,bins='fd',edgecolor='black', color='skyblue',density=True,label='Histograma de Temperatura')

#gráfica de densidad
plt.plot(val_x,val_y, color='red',label='Línea de densidad gaussiana',linewidth=2.5)


plt.title('Histograma de Temperatura', fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.ylabel('Cantidad de datos', fontsize=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
