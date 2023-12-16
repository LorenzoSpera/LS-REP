import numpy as np
import scipy
import matplotlib.pyplot as plt 
import math
import pandas as pd 
import sys, os 
""" script in python che richiama il modlulo creato nello script modulo_montecarlo1.py"""

sys.path.append('/Users/lorenzospera/Desktop/modulo_montecarlo1.py')
import modulo_montcarlo1
from modulo_montcarlo1 import random_walk_2d

lista_array_x = []
lista_array_y = []
s = 1
N = 1000
passi= np.arange(0,1000)

distanze_x = []   # lista che contiene le distanze sulle x dei random walker 
distanze_y = []   # lista che contiene le distanze sulle y dei random walker 


for i in range(5):
    x = random_walk_2d(s,N)[0]
    y = random_walk_2d(s,N)[1]
    distanze_x.append(x)
    distanze_y.append(y)

plt.plot(passi, distanze_x[0] )
plt.show()

grafico_1 = int(input('1 se si vuole visualizzare il grafico 2d che mostra i 5 random walker: '))
if (grafico_1==1):
    plt.figure(figsize=[10,8])
    for i in range(5):
        plt.title('Grafico in 2d dei 5 random walker', c='darkred', fontsize = 12)
        plt.plot(distanze_x[i], distanze_y[i], label='Random walker {:}'.format(i))
        plt.legend(loc='upper right')
    plt.show()
distanze_10x  = []
distanze_10y  = []
distanze_100x = []
distanze_100y = []
distanze_1000x = []
distanze_1000y = []
lista_passi = [10,100,1000]
for n in lista_passi:
    if (n==10):
        for i in range (100):
            distanze_10x.append(random_walk_2d(s,10)[0])
            distanze_10y.append(random_walk_2d(s,10)[1])
    if (n==100):
        for i in range(100):
            distanze_100x.append(random_walk_2d(s,100)[0])
            distanze_100y.append(random_walk_2d(s,100)[1])
    if (n==1000):
        for i in range(100):
            distanze_1000x.append(random_walk_2d(s,1000)[0])
            distanze_1000y.append(random_walk_2d(s,1000)[1])


posizioni_10x_finali = []
posizioni_10y_finali = []
posizioni_100x_finali = []
posizioni_100y_finali = []
posizioni_1000x_finali = []
posizioni_1000y_finali = []

""" nelle liste appena defnite vengono salvate i punti iniziali e finali delle distanze
percorse lungo x e lungo y per ogni random walker che fa 10, 100 e 1000 passi"""
for i in range(len(distanze_1000x)):
    posizioni_10x_finali.append(distanze_10x[i][-1])
    posizioni_10y_finali.append(distanze_10y[i][-1])
    posizioni_100x_finali.append(distanze_100x[i][-1])
    posizioni_100y_finali.append(distanze_100y[i][-1])
    posizioni_1000x_finali.append(distanze_1000x[i][-1])
    posizioni_1000y_finali.append(distanze_1000y[i][-1])
grafic0_2 = int(input('1 se si vuole visualizzare il grafico delle distribuzioni: '))
if (grafic0_2==1):
    plt.figure(figsize=[10,8])
    plt.title('Distribuzione delle posizioni finali per i 100 random walker con 10, 100 e 1000 passi')
    plt.plot(posizioni_10x_finali, posizioni_100y_finali,".", c='darkred',label='10 passi')
    plt.plot(posizioni_100x_finali, posizioni_100y_finali,".", c='darkblue',label='100 passi')
    plt.plot(posizioni_1000x_finali, posizioni_1000y_finali,".", c='green',label='1000 passi')
    plt.legend(loc='upper right')
    plt.show()


# riferendoci al primo grafico, calcoliamo il quadrato della distanza per i 5 random walker 
print(distanze_x[0][1])
quadrato_distanza_1 = []
quadrato_distanza_2 = []
quadrato_distanza_3 = []
quadrato_distanza_4 = []
quadrato_distanza_5 = []
for j in range(1000):
    d1_quadro = distanze_x[0][j]**2+distanze_y[0][j]**2
    d2_quadro = distanze_x[1][j]**2+distanze_y[1][j]**2
    d3_quadro = distanze_x[2][j]**2+distanze_y[2][j]**2
    d4_quadro = distanze_x[3][j]**2+distanze_y[3][j]**2
    d5_quadro = distanze_x[4][j]**2+distanze_y[4][j]**2
    quadrato_distanza_1.append(d1_quadro)
    quadrato_distanza_2.append(d2_quadro)
    quadrato_distanza_3.append(d3_quadro)
    quadrato_distanza_4.append(d4_quadro)
    quadrato_distanza_5.append(d5_quadro)

andam = int(input(" 1 per visualizzare l'andamento del quadrato della distanza in funzione dei passi: "))
if (andam==1):
    plt.figure(figsize=[10,8])
    plt.title('Andamento del quadrato della distanza in funzione dei passi ', c='darkred', fontsize = 12)
    plt.plot(passi, quadrato_distanza_1, c='darkred', label='Random walker 1')
    plt.plot(passi, quadrato_distanza_2 ,c='darkblue', label='Random walker 2')
    plt.plot(passi, quadrato_distanza_3, c='green', label='Random walker 3')
    plt.plot(passi, quadrato_distanza_4, c='magenta', label='Random walker 4')
    plt.plot(passi, quadrato_distanza_5, c='deepskyblue', label='Random walker 5')
    plt.legend(loc='upper right')
    plt.show()

plt.show()
confronto_quad = int(input("1 se si vuole visualizzare il confronto tra lo spostamento nel piano e il quadrato della distanza percorsa: "))
if (confronto_quad==1):
    fig, ax = plt.subplots(1,2, figsize=[12,6])
    for i in range(5):
            ax[0].plot(distanze_x[i], distanze_y[i], label='Random walker {:}'.format(i))
            ax[0].legend(loc='upper left')
    ax[0].set_title('Grafico 2d dei 5 random waker', fontsize=12)
    ax[1].set_title('Andamento del quadrato della distanza ', fontsize=12)
    ax[1].plot(passi, quadrato_distanza_1, label='Random walker 1')
    ax[1].plot(passi, quadrato_distanza_2, label='Random walker 2')
    ax[1].plot(passi, quadrato_distanza_3, label='Random walker 3')
    ax[1].plot(passi, quadrato_distanza_4, label='Random walker 4')
    ax[1].plot(passi, quadrato_distanza_5, label='Random walker 5')
    ax[0].set_xlabel('Numero passi')
    ax[1].set_xlabel('Numero passi')
    ax[0].set_ylabel('Posizione nel piano')
    ax[1].set_ylabel('Quadrato della distanza')
    ax[1].legend(loc='upper right')
    plt.show()
