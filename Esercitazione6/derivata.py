import numpy as np 
import scipy 
from scipy import integrate
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft

import math
import pandas as pd 
import matplotlib.pyplot as plt
import argparse

data = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/Esercitazione6/oscilloscope.csv')
print(data)

time = data['time']*0.001
signal1 = data['signal1']
signal2 = data['signal2']
print(time[0])



fig, (ax1, ax2) = plt.subplots(1,2, figsize= [8,6])
ax1.plot(time, signal1, label='Segnale1')
ax2.plot(time, signal2, label='Segnale2')
ax1.set_xlabel('Time(s)')
ax1.set_ylabel('Voltaggio(V)')
ax2.set_xlabel('Time(s)')
ax2.set_ylabel('Voltaggio(V)')
plt.legend()
plt.show()


# Funzione che implementa una versione della differenza centarle 
# f'(i) =  [f(i+1)-f(i-1)] / [x(i+1)-x[i-1]]

def derivata_centrale(s,t):
    """funzione che calcola la derivata"""
    derivata = []
    for i in range(0,len(s)-2):
        num = s[i+2]-s[i]
        den = t[i+2]-t[i]
        derivata.append(num/den)
    return derivata 

derivata1 = derivata_centrale(signal1,time)
derivata2 = derivata_centrale(signal2,time)



# fig, ax = plt.subplots(1,2, figsize= [8,6])
# fig.suptitle('Derivata calcolata con la funzione')
# ax[0].plot(time[:-2], derivata1, label='Derivata 1')
# ax[1].plot(time[:-2], derivata2, label='Derivata 2')
# ax[0].set_xlabel('Time(s)')
# ax[0].set_ylabel('Derivata(V/s)')
# ax[1].set_xlabel('Time(s)')
# ax[1].set_ylabel('Derivata(V/s)')
# for a in ax:
#     a.legend(loc='upper right')
# plt.legend()
# plt.show()

# derivata calcolata con i gradiente 

# gradiente1 = np.gradient(signal1)
# gradiente2 = np.gradient(signal2)
# fig, ax = plt.subplots(1,2, figsize= [8,6])
# fig.suptitle('Derivata calcolata con numpuy')
# ax[0].plot(time, gradiente1, label='Derivata 1')
# ax[1].plot(time, gradiente1, label='Derivata 2')
# ax[0].set_xlabel('Time(s)')
# ax[0].set_ylabel('Derivata(V/s)')
# ax[1].set_xlabel('Time(s)')
# ax[1].set_ylabel('Derivata(V/s)')
# for a in ax:
#     a.legend(loc='upper right')
# plt.legend()
# plt.show()

# le trasformate funzionano solo con array di numpy 
# segnale1np = np.array(signal1)
# signal1fft = fft(segnale1np)
# freq = fftfreq(len(signal1fft), 1/len(signal1fft))

# module = pow(np.abs(signal1fft),2)
# plt.plot(freq, module)
# plt.xlim(0,500)
# plt.show()

# massimo = np.max(module)

# maschera = module == massimo

# filtrato = module*maschera
# plt.plot(freq, filtrato)
# plt.xlim(0,50)
# plt.show()

# segnale_filtrato = ifft(filtrato)
# segnale_derivato = np.gradient(segnale_filtrato)



# fig, ax = plt.subplots(1,2, figsize= [8,6])
# fig.suptitle('Derivata calcolata con numpuy')
# ax[0].plot(time, segnale_filtrato, label='Derivata 1')
# ax[1].plot(time, segnale_derivato, label='Derivata 2')
# ax[0].set_xlabel('Time(s)')
# ax[0].set_ylabel('Derivata(V/s)')
# ax[1].set_xlabel('Time(s)')
# ax[1].set_ylabel('Derivata(V/s)')
# for a in ax:
#     a.legend(loc='upper right')
# plt.legend()
# plt.show()


segnale1 = np.array(signal1)
print(segnale1[-1])

def derivata_centrale2(s,t,n=2):
    """funzione che calcola la derivata"""
    derivata = []
    elemento = (segnale1[0]-segnale1[len(segnale1)-1])/(time[0]-time[len(segnale1)-1])
    derivata.append(elemento)
    # sulla funzione precedente ho fatto -2 quindi qua faccio -n/2 per non sforare
    for i in range(1,len(s)-int(n/2)):
        num = s[i+int(n/2)]-s[i-int(n/2)]
        den = t[i+int(n/2)]-t[i-int(n/2)]
        derivata.append(num/den)
    return derivata 


derivata_prova = derivata_centrale2(segnale1, time)
plt.plot(time[1:], derivata_prova)
plt.show()























