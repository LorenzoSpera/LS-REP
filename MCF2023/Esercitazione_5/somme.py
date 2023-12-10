import math 
import numpy as np 
# funzione che somma i primi numeri naturali 


def somma_numeri(n):
    somma = 0
    for i in range(0,n+1):
        somma = somma+i
    return somma
        

# funzione che somma le radici dei primi numeri naturali 

def somma_radici(n):
    sommar = 0
    for i in range(0,n+1):
        sommar = sommar + math.sqrt(i)
    return sommar

# funzione che resituisce somma e prodotto contemporaneamente

def somma_e_prodotto(n):
    somma = 0
    prodotto = 1
    for i in range(1,n+1):
        somma = somma +i 
        prodotto = prodotto*i
    return somma, prodotto

def somma_alpha(n, alpha=1):
    somma= 0
    for i in range(0,n+1):
        somma= somma+i**alpha
    return somma



        
