import numpy as np
import scipy 
from scipy import integrate
import pandas as pd
import matplotlib.pyplot as plt 
import math

x = np.arange(-5,5.05, 0.1)
v = 0.1*x**6
#print(v)
plt.plot(x, v, color='mediumblue')
plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel(r'V(x)')
plt.plot(4.5, 0.1*4.5**6, 'o', markersize=12, color='red')
plt.show()

maschera = x>=0
estremi = x[maschera]
def v(x):
    return 0.1*x**6
k = 0.1
m = 0.5
periodi = []
vv = 0.1*estremi**6

for i in range(3,len(estremi)+1):
    
    v_0 = v(estremi[i-1])
    integranda = math.sqrt(8*m)/(np.sqrt(v_0-v(estremi)))
    periodi.append(scipy.integrate.simpson(integranda[:i-1],estremi[:i-1],dx=5))
plt.title('Andamento del periodo in funzione della posizione x_0')
plt.plot(estremi[:-2], periodi, c='mediumblue')
plt.xlabel('x_0')
plt.ylabel('Periodo')
plt.show()

def v2(x):
    return x**2

periodi2 = []
for i in range(2, len(estremi)):
    V_0 = v(estremi[i])
    integranda = math.sqrt(8*m)/(np.sqrt(v_0-v(estremi)))
    periodi2.append(scipy.integrate.simpson(integranda[:i],estremi[:i]))

plt.title('Andamento del periodo in funzione della posizione x_0')
plt.plot(estremi[2:], periodi2, c='mediumblue')
plt.xlabel('x_0')
plt.ylabel('Periodo')
plt.show()










