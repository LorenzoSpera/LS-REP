import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import sys,os 

import reco
sys.path.append('reco.py')
#lettura dati da csv 
data0 = pd.read_csv('hit_times_M0.csv')
data1 = pd.read_csv('hit_times_M1.csv')
data2 = pd.read_csv('hit_times_M2.csv')
data3 = pd.read_csv('hit_times_M3.csv')

def crea_array(file):
    hits = []
    for i in range(0,len(file['hit_time'])):
        hits.append(reco.hit(file['mod_id'][i],file['det_id'][i],file['hit_time'][i]))
    return hits

array_0 = crea_array(data0)
array_1 = crea_array(data1)
array_2 = crea_array(data2)
array_3 = crea_array(data3)

array_completo = []
for e1, e2, e3, e4 in zip(array_0, array_1, array_2, array_3):
    array_completo.append(e1)
    array_completo.append(e2)
    array_completo.append(e3)
    array_completo.append(e4)

array_completo_nuovo = np.sort(array_completo)

differenze_finali = np.diff(array_completo_nuovo)
plt.figure(figsize=[8,8])
plt.title('Istogramma della distribuzione differenze array completo')
n, bins, p = plt.hist(differenze_finali, bins=150, color='red', alpha=0.7 )
plt.xlabel('Differenze tempi', fontsize=16)
plt.show()

maschera = differenze_finali>0
differenze_finali_maschera = differenze_finali[maschera]
logaritmi = np.log10(np.float64(differenze_finali_maschera))

plt.figure(figsize=[8,8])
plt.title('Istogramma della distribuzione differenze logaritmi array completo')
n, bins, p = plt.hist(logaritmi, bins=150, color='red', alpha=0.7 )
plt.xlabel('Differenze logaritmi tempi', fontsize=16)
plt.yscale('log')
plt.show()




















