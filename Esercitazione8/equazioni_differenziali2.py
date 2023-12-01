import pandas as pd
import scipy 
import numpy as np
import matplotlib.pyplot as plt 
import  matplotlib.colors 


""" le due equazioni differenziali simultanee sono date da 
   dtheta/dt = omega        domega/dt = -g/lsin(theta)"""


g = 9.81    # costanti che compaiono nell'equazione
l = 0.5
omega_0 = 0
theta_0 = np.pi/4    # condizioni iniziali 
time = np.linspace(0, 10, 1000)

def fode(r, t, g, l):
    theta = r[0]
    omega = r[1]
    ftheta = omega 
    fomega = -g*np.sin(theta)/l
    return np.array([ftheta,fomega], float)


r_in = [theta_0, omega_0]

soluzione = scipy.integrate.odeint(fode, r_in, time, args = (g,l) )
grafico_theta_omega = int(input('1 se si vuole visualizzare il grafico di theta e di omega: '))
if (grafico_theta_omega==1):
    plt.figure(figsize=[8,8])
    plt.title('Andamento delle soluzioni in funzione del tempo ',c='darkred', fontsize =12)
    plt.plot(time, soluzione, label = ('theta','omega'))
    plt.xlabel('Time(s)')
    plt.ylabel('Theta(t) / Omega(t)')
    plt.legend(loc='upper right')
    plt.show()


theta_t = soluzione[:,0]
grafico_theta = int(input('1 se si vuole visualizzare il grafico di omega in funzione di t: '))
if (grafico_theta==1):
    plt.figure(figsize=[8,8])
    plt.title('Andamento della soluzione in funzione del tempo ',c='darkred', fontsize =12)
    plt.plot(time, theta_t, c='mediumblue', label='Theta(t)')
    plt.xlabel('Time(s)')
    plt.ylabel('Theta(t)')
    plt.legend(loc='upper right')
    plt.show()


# risolviamo ora l'equazione per diverse condizioni iniziali 
soluzione_2 = scipy.integrate.odeint(fode, r_in, time, args = (g,1) ) # stesse condizioni iniziali con l = 1
r_in3 = [np.pi/6, 0]
soluzione_3 = scipy.integrate.odeint(fode, r_in3, time, args = (g,0.5) ) # angolo inziale diverso 30 gradi
theta_t2 = soluzione_2[:,0]
theta_t3 = soluzione_3[:,0]

confronto_3_theta =  int(input('1 se si vogliono visualizzare le tre soluzioni: '))
if (confronto_3_theta==1):
    plt.figure(figsize=[8,8])
    plt.title('Andamento delle 3 soluzioni in funzioni del tempo ',c='darkred', fontsize =12)
    plt.plot(time, theta_t, c='mediumblue', label='Theta(t)')
    plt.plot(time, theta_t2, c='red', label='Theta_1(t)')
    plt.plot(time, theta_t3, c='teal', label='Theta_2(t)')
    plt.xlabel('Time(s)')
    plt.ylabel('Theta_i(t)')
    plt.legend(loc='upper right')
    plt.show()

confronto_3_theta_2=  int(input('1 se si vogliono visualizzare le tre soluzioni: '))
if (confronto_3_theta_2==1):
    fig, ax = plt.subplots(3,1, sharex=True, figsize =[10,8])
    ax[0].plot(time, theta_t, c='mediumblue', label='Theta(t)')
    ax[1].plot(time, theta_t2, c='red', label='Theta1(t)')
    ax[2].plot(time, theta_t3, c='purple', label='Theta2(t)')
    ax[0].set_ylabel('Theta(t)')
    ax[1].set_ylabel('Theta1(t)')
    ax[2].set_ylabel('Theta2(t)')
    ax[2].set_xlabel('Time(s)')
    plt.show()






