import pandas as pd
import scipy 
import numpy as np
import matplotlib.pyplot as plt 
import  matplotlib.colors 

""" scrivere uno script che risolva l'equazione differenziale dell'oscillatore anarmonico con diverse
condizioni iniziali e confrontare graficamente i risultati"""

k = 300
m = 0.3                 # costanti che compaiono nell'equazione differenziale 
omega = np.sqrt(k/m) 
time = np.linspace(0,10,1000)

# l'equazione differenziale è data da d^2x/dt^2 = -omega^2x^3

def fode(r,t, k, m ):
    """ funzione che restituisce l'equazione differenziale
    r è il vettore che contiene le due soluzioni 
    la derivata prima e seconda di x"""
    x = r[0]
    y = r[1] # con y = dx/dt
    fx =y
    fy = -(k/m)*x**3
    return np.array([fx,fy], float)

x_0 = 0.3
y_0 = 0
r_in_0 = [x_0,y_0]

soluzione = scipy.integrate.odeint(fode, r_in_0, time, args=(k,m))
grafico_pos_e_vel = int(input('1 se si vuole visualizzare il grafico della posizione e della velocità :'))
if (grafico_pos_e_vel==1):
    plt.figure(figsize=[8,8])
    plt.title('Posizione e velocità in funzione del tempo', c='darkred', fontsize = 12)
    plt.plot(time, soluzione, label=(('x(t)','v(t)')))
    plt.xlabel('Time(s)')
    plt.ylabel('x(t)/v(t)')
    plt.legend(loc='upper right')
    plt.show()

legge_oraria = soluzione[:,0] # dalla soluzione si estrae la prima colonna che rappresenta le x 

grafico_pos = int(input('1 se si vuole visualizzare il grafico della posizione :'))
if (grafico_pos==1):
    plt.figure(figsize=[8,8])
    plt.title('Posizione e velocità in funzione del tempo', c='darkred', fontsize = 12)
    plt.plot(time, legge_oraria, label='x(t)',c = 'darkred')
    plt.xlabel('Time(s)')
    plt.ylabel('x(t)')
    plt.legend(loc='upper right')
    plt.show()


r_in_1 = [0.2,0.5]
r_in_2 = [0.4,0.5]
soluzione_2 = soluzione = scipy.integrate.odeint(fode, r_in_1, time, args=(k,m))
soluzione_3 = soluzione = scipy.integrate.odeint(fode, r_in_2, time, args=(k,m))
legge_oraria_2 = soluzione_2[:,0]
legge_oraria_3 = soluzione_3[:,0]

# confronto delle 3 soluzioni sullo stesso grafico
confronto_soluzioni = confronto_condizioni_inziali = int(input('1 se si vuole visualizzare il confronto delle 3 soluzioni con c.i diverse: '))
if (confronto_soluzioni==1):
    plt.figure(figsize=[8,8])
    plt.title('Confronto delle 3 soluzioni con condizioni iniziali diverse', c='darkred')
    plt.plot(time, legge_oraria, label='x_0={:.2f}m  y_0={:.2f}m/s'.format(r_in_0[0],r_in_0[1]))
    plt.plot(time, legge_oraria_2, c='sienna', label='x_0={:.2f}m y_0={:.2f}m/s'.format(r_in_1[0],r_in_1[1]))
    plt.plot(time, legge_oraria_3, c='green', label='x_0={:.2f}m  y_0={:.2f}m/s'.format(r_in_2[0],r_in_2[1]))
    plt.xlabel('Time(s)')
    plt.ylabel('x_i(t)')
    plt.legend(loc='upper right')
    plt.show()

# confronto delle 3 soluzioni con condizioni inziali 
confronto_condizioni_inziali = int(input('1 se si vuole visualizzare il confronto delle 3 soluzioni con c.i diverse: '))
if (confronto_condizioni_inziali==1):
    fig, ax = plt.subplots(3,1, sharex=True, figsize =[10,8])
    fig.suptitle('3 soluzioni con condizioni iniziali diverse', c='darkred', fontsize=12)
    ax[0].plot(time, legge_oraria, c='mediumblue', label='x_0={:.2f} e y_0={:.2f}'.format(r_in_0[0],r_in_0[1]))
    ax[1].plot(time, legge_oraria_2, c='red', label='x_0={:.2f} e y_0={:.2f}'.format(r_in_1[0],r_in_1[1]))
    ax[2].plot(time, legge_oraria_3, c='purple', label='x_0={:.2f} e y_0={:.2f}'.format(r_in_2[0],r_in_2[1]))
    ax[0].set_ylabel('x_1(t)')
    ax[0].legend(loc='upper right')
    ax[1].legend(loc='upper right')
    ax[2].legend(loc='upper right')
    ax[1].set_ylabel('x_2(t)')
    ax[2].set_ylabel('x_3(t)')
    ax[2].set_xlabel('Time(s)')
    plt.show()


# facciamo la stessa cosa cambiando il valore della costante elastica ma partendo dalle stesse condizioni iniziali 

r_iniziali = [0.5,0]
k1 = 10
k2 = 100
k3 = 1000
soluzione_k1 = scipy.integrate.odeint(fode, r_iniziali, time, args=(k1,m))
soluzione_k2 = scipy.integrate.odeint(fode, r_iniziali, time, args=(k2,m))
soluzione_k3 = scipy.integrate.odeint(fode, r_iniziali, time, args=(k3,m))
x_k1 = soluzione_k1[:,0]
x_k2 = soluzione_k2[:,0]
x_k3 = soluzione_k3[:,0]

confronto_k = int(input("1 se si vuole visualizzare l'andamento nel tempo in funzione di k "))
if (confronto_k==1):
    plt.figure(figsize=[10,6])
    plt.title('Andamento nel tempo in funzione della costante elastica con condizioni inziali x_0={:.2f} e v_0={:.2f}'.format(r_iniziali[0],r_iniziali[1]),c='darkred')
    plt.plot(time, x_k1, c='indigo', label='k={:.1f}'.format(k1))
    plt.plot(time, x_k2, c='khaki', label='k={:.1f}'.format(k2))
    plt.plot(time, x_k3, c='steelblue', label='k={:.1f}'.format(k3))
    plt.xlabel('Time(s)')
    plt.ylabel('x(t)')
    plt.legend(loc='upper right')
    plt.show()
    


