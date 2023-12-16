import numpy as np
import scipy
import matplotlib.pyplot as plt 
import math
import pandas as pd 


"""modulo che definisce una procedura di random walk in due dimensioni con le seguenti caratterisiche
la diffusione ha un passo costante s """



def random_walk_2d(s,N):
    """ funzione che a partire dal passo costante restituisce
    due array che contengono le distanze percorse lungo x e lungo y
    dopo n passi;
    con check viene generato un angolo casuale nell'intervallo 0 2pi,dato che questi valori
    sono equiprobabili """
    distanza_percorsa_x = np.array([])
    distanza_percorsa_y = np.array([])
    deltax = 0
    deltay = 0
    check = np.random.uniform(low =0 , high= 2*np.pi, size = N)
    for phi in check:
            deltax += s*np.cos(phi)
            deltay += s*np.sin(phi)
            distanza_percorsa_x = np.append(distanza_percorsa_x, deltax)
            distanza_percorsa_y = np.append(distanza_percorsa_y, deltay)
            #posizione.append(distanza_percorsa_x, distanza_percorsa_y)
    return (distanza_percorsa_x,distanza_percorsa_y)



def random_walk_2d_asimmetrica_con_passo(s,s_f):
    """ funzione che a partire dal passo costante restituisce
    due array che contengono le distanze percorse lungo x e lungo y
    dopo n passi;
    con check viene generato un angolo casuale nell'intervallo 0 2pi,dato che questi valori
    sono equiprobabili """
    distanza_percorsa_x = np.empty(0)
    distanza_percorsa_y = np.empty(0)
    deltax = 0
    deltay = 0
    while (abs(deltax)<200*s):
        phi = np.random.uniform(low=0, high=2*np.pi)
        deltax += s*np.cos(phi) + s_f
        deltay += s*np.sin(phi)
        distanza_percorsa_x = np.append(distanza_percorsa_x, deltax)
        distanza_percorsa_y = np.append(distanza_percorsa_y, deltay)    
    return (distanza_percorsa_x,distanza_percorsa_y)
      

def random_walk_2d_asimmetrica(s,N):
    """ funzione che a partire dal passo costante restituisce
    due array che contengono le distanze percorse lungo x e lungo y
    dopo n passi;
    con check viene generato un angolo casuale nell'intervallo 0 2pi,dato che questi valori
    sono equiprobabili """
    distanza_percorsa_x = np.array([])
    distanza_percorsa_y = np.array([])
    deltax = 0
    deltay = 0
    phi_generated = np.random.random(N)
    check = 2*np.arccos(1-2*phi_generated)
    for phi in check:
                deltax += s*np.cos(phi) 
                deltay += s*np.sin(phi)
                distanza_percorsa_x = np.append(distanza_percorsa_x, deltax)
                distanza_percorsa_y = np.append(distanza_percorsa_y, deltay)  
    return (distanza_percorsa_x,distanza_percorsa_y)

  
