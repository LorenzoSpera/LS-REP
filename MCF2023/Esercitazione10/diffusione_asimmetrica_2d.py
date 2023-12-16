import numpy as np
import scipy
import matplotlib.pyplot as plt 
import math
import pandas as pd 
import sys, os 

""" script python che implememta sempre il modulo montecarlo ma utilizza la versione asimmetrica"""
sys.path.append('/Users/lorenzospera/Desktop/modulo_montecarlo1.py')
import modulo_montcarlo1
from modulo_montcarlo1 import random_walk_2d_asimmetrica
from modulo_montcarlo1 import random_walk_2d_asimmetrica_con_passo
s = 1
N = 1000
passi= np.arange(0,1000)

distanze_x = []   # lista che contiene le distanze sulle x dei random walker 
distanze_y = []   # lista che contiene le distanze sulle y dei random walker 


for i in range(5):
    x = random_walk_2d_asimmetrica(s,N)[0]
    y = random_walk_2d_asimmetrica(s,N)[1]     # 5 random walker con diffusione asimmetrica per 1000 passi
    distanze_x.append(x)
    distanze_y.append(y)


grafico_random_walker = int(input('1 se si vuole visualizzare la posizione dei 5 random walker: '))
if (grafico_random_walker==1):
    plt.figure(figsize=[10,8])
    for i in range(5):
        plt.title('Posizione nel piano dei 5 random walker', c='darkred', fontsize=12)
        plt.plot(distanze_x[i], distanze_y[i], label='Random walker {:.2f}'.format(i))
        plt.xlabel('Posizione lungo x')
        plt.ylabel('Posizione lungo y')
        plt.legend(loc='upper right')
    plt.show()


sf_1 = 1
sf_2 = 0.001

# distanze_x_sf1 = []
# distanze_y_sf1 = []
# distanze_x_sf2 = []
# distanze_y_sf2 = []
# for i in range(5):
#     xx = random_walk_2d_asimmetrica_con_passo(s, sf_1)
#     yy = random_walk_2d_asimmetrica_con_passo(s, sf_1)
#     xx2 = random_walk_2d_asimmetrica_con_passo(s, sf_2)
#     yy2 = random_walk_2d_asimmetrica_con_passo(s, sf_2)
#     distanze_x_sf1.append(xx)
#     distanze_y_sf1.append(yy)
#     distanze_x_sf2.append(xx2)
#     distanze_y_sf2.append(yy2)
# plt.plot(distanze_x_sf1[0], distanze_y_sf1[0])
# plt.show()
x_sf1, y_sf1 = random_walk_2d_asimmetrica_con_passo(s,sf_1)

x_sf2 , ysf_2 = random_walk_2d_asimmetrica_con_passo(s,sf_2)

plt.title('Confronto tra diversi passi: ')
plt.plot(x_sf1, y_sf1, label='sf={:.5f}'.format(sf_1))
plt.plot(x_sf2, ysf_2,label='sf={:.5f}'.format(sf_2))
plt.show()


# confronto_sf = int(input('1 se si vuole confrontare il grafico con i due diversi sf: '))
# if (confronto_sf==1):
#     fig , ax = plt.subplots(2,1, figsize=[10,8])
#     fig.suptitle('Confronto grafico con i due fs ')
#     for i in range(5):
#         ax[0].plot(distanze_x_sf1[i],distanze_y_sf1[i], label='Random walker e s_f =0.1')
#         ax[1].plot(distanze_x_sf2[i],distanze_y_sf2[i], label='Random walker e s_f =0.01')
#     ax[0].set_xlabel('Posizione lungo x')
#     ax[1].set_xlabel('Posizione lungo x')
#     ax[0].set_ylabel('Posizione lungo y')
#     ax[1].set_ylabel('Posizione lungo y')
#     ax[0].legend(loc='upper right')
#     ax[1].legend(loc='upper right')
#     plt.show()