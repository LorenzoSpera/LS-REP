import numpy as np
import scipy
import matplotlib.pyplot as plt 
import math
import pandas as pd 
from scipy import optimize
import sys, os 

""" script che genera una distribuzione di probabilità del tipo p(phi)= 1/4 sin(phi/2)"""

# nella definizione della cumulativa, l'integrale a denominatore è 1 

# il numeratore è -1/2(cos(phi/2)+1)
def cumulativa(x):
    """ funzione che restituisce la funzione cumulativa, con x in 0 2pi"""
    return -(np.cos(x)+1)/2


# l'inversa della comulativa è 2 arccos(-2*phi-1)

def inv_cumulativa(x):
    """ funzione che restituisce l'inverso della funzione cumulativa """
    return 2*np.arccos(1-2*x)

# grafico inversa cumulativa della funzione onda quadra nell'intervallo (0,5)
yc  = np.arange(0,1, 0.001)
xc  = inv_cumulativa(yc)
# grafico dell'inversa della cumulativa
cumulativa_graf = int(input('1 se si vuole visualizzare il grafico dell inversa della cumulativa: '))
if (inv_cumulativa==1):
    plt.figure(figsize=[10,8])
    plt.plot(yc, xc, color='darkcyan')
    plt.grid()
    plt.xlabel('y')
    plt.ylabel(r'$c^{-1}$(y)')
    plt.show()
nsamples = 100000
# valri y distribuiti uniformemnte in (0-1)
yrndq = np.random.random(nsamples)
# valori x da cumulativa inversa
xrndq = inv_cumulativa(yrndq)

fig, ax = plt.subplots(1,2, figsize=(10,8))
ax[0].hist(yrndq, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(xrndq, bins=100, range=(0,2*np.pi), color='orange', ec='darkorange')
ax[1].set_title('Distribuzione secondo la funzione definita')
ax[1].set_xlabel('x')
plt.show()

n , bins , p =  plt.hist(xrndq, bins=100, color='darkred', label='distribuzione generata')
bincenters = (bins[:-1] + bins[1:])/2

def test_func(x,A):
    return A*np.sin(x/2)
pstart = [0.25]
params, params_covariance = optimize.curve_fit(test_func, xdata=bincenters, ydata=n,sigma=np.sqrt(n), p0=pstart)
# print('params', params )
# print('params_cov', params_covariance)
# print('errori params', np.sqrt(params_covariance.diagonal()))

#n, bins, p = plt.hist(xrndq, bins=200, color='darkred', label='distribuzione generata')
confronto = int(input('1 se si vuole visualizzare il fit della distribuzione: '))
if (confronto==1):
    plt.title('Fit dei dati ')
    plt.plot(bincenters, test_func(bincenters,params[0]), label='fit della distribuzione', c='darkblue')
    plt.xlabel('X')
    plt.ylabel('Eventi / Bin')
    plt.legend(loc='upper right')
    plt.show()

sys.path.append('/Users/lorenzospera/Desktop/modulo_montecarlo1.py')
import modulo_montcarlo1
from modulo_montcarlo1 import random_walk_2d_asimmetrica

s = 1
N = 1000
passi= np.arange(0,1000)

distanze_x = []   # lista che contiene le distanze sulle x dei random walker 
distanze_y = []   # lista che contiene le distanze sulle y dei random walker 


for i in range(5):
    x = random_walk_2d_asimmetrica(s,N)[0]
    y = random_walk_2d_asimmetrica(s,N)[1]
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