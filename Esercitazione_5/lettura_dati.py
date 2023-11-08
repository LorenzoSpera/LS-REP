import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

#lettura dati da csv 
data0 = pd.read_csv('hit_times_M0.csv')
data1 = pd.read_csv('hit_times_M1.csv')
data2 = pd.read_csv('hit_times_M2.csv')
data3 = pd.read_csv('hit_times_M3.csv')

# print dei dati per vedere il nome delle colonne 
#print(data0)

# istogramma dei tempi 
plt.figure(figsize=[8,8])
plt.title('Istogramma della distribuzione tempi per data0')
n, bis, p = plt.hist(data0['hit_time'], bins=150, color='red', alpha=0.7 )
plt.xlabel('Tempi di hit', fontsize=16)
plt.show()

# creiamo l'array contenente le differenze tra due tempi consecutivi 

differenze = np.diff(data0['hit_time'])
maschera = differenze>0
#differenze = differenze*maschera
logaritmo_differenze = np.log10(differenze[maschera])
plt.figure(figsize=[8,8])
plt.title('Distribuzione dei logaritmi delle differenze')
n, bis, p = plt.hist(logaritmo_differenze, bins=150, color='red', alpha=0.7 )
plt.xlabel('Logaritmo delle differze di tempi consecutivi', fontsize=16)
plt.show()
plt.show()



