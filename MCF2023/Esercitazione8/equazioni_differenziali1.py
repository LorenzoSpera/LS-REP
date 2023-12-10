import pandas as pd
import scipy 
import numpy as np
import matplotlib.pyplot as plt 
import  matplotlib.colors 

# vari parametri per la risoluzione dell'equazione differenziale
V_in = 0.5
rc = 1 
a = 0
b = 10
n = 1000
h = (b-a)/n
v_0 = 0
x = v_0

tt = np.arange(a, b , h)

def fode(x,t):
    """funzione che definisce l'equazione differenziale"""
    return (V_in-x)/rc
xx = np.empty(0)
eulero = int(input('1 per visualizzare il grafico con il metodo di eulero : '))
if (eulero==1):
    
    for t in tt:
        xx = np.append(xx, x)
        x = x +h*fode(x,t)


    # grafichiamo i risultati 

    
    plt.figure(figsize=[8,8])
    plt.title('Andamento della soluzione in funzione del tempo') 
    plt.plot(tt, xx, label='RC=1')
    plt.xlabel('Time(s)')
    plt.ylabel('V_out(V)')
    plt.legend(loc='upper right')
    plt.show()

xx1 = np.empty(0)
runge_kutta1 = int(input('1 per visualizzare il grafico con il metodo di rungekutta : '))
if (runge_kutta1==1):
    # facciamo lo stesso con il metodo runge kutta al quarto ordine
    for t in tt:
        xx1 = np.append(xx1, x)
        k1 = h*fode(x,t)
        k2 = h*fode(x+0.5*k1,t+0.5*h)
        k3 = h*fode(x+0.5*k2,t+0.5*h)
        k4 = h*fode(x+k3,t+h)
        x = x+(k1+k1*2+k3*2+k4)/6
    
    plt.figure(figsize=[8,8])
    plt.title('Andamento della soluzione in funzione del tempo') 
    plt.plot(tt, xx1, label ='RC=1')
    plt.xlabel('Time(s)')
    plt.ylabel('V_out(V)')
    plt.legend(loc='upper right')
    plt.show()


xx_eulero = np.empty(0)
xx_kutta = np.empty(0)
for t in tt:
        xx_eulero= np.append(xx_eulero, x)
        x = x +h*fode(x,t)
x1 = 0
for t in tt:
        xx_kutta = np.append(xx_kutta, x1)
        k1 = h*fode(x1,t)
        k2 = h*fode(x1+0.5*k1,t+0.5*h)
        k3 = h*fode(x1+0.5*k2,t+0.5*h)
        k4 = h*fode(x1+k3,t+h)
        x1 = x1+(k1+k1*2+k3*2+k4)/6

# per visualizzare la differenza dei due metodi definiamo gli scarti come segue


grafico_3 = int(input('1 se si vuole visualizzare il confronto tra i due grafici: '))
if (grafico_3==1):
     img, ax = plt.subplots(figsize=(10,7))
     plt.title('Confronto della soluzione con i due metodi ')
     plt.plot(tt, xx_eulero, label ='Eulero' ,c='mediumblue')
     plt.plot(tt, xx_kutta, label='Runge-Kutta ', c='red')
     plt.xlabel('Time(s)')
     plt.ylabel('Voltaggio(V)')
     plt.legend(loc='lower left')
     ins = ax.inset_axes([0.45, 0.45, 0.32,0.37])
     ins.set_title('Zoom sui due metodi')
     ins.plot(tt, xx_eulero, color= 'mediumblue',linewidth=1)
     ins.plot(tt,xx_kutta, color= 'red', linewidth=1 )
     ins.set_ylim(0.1430,0.1470)
     ins.set_xlim(0.335,0.343)
     plt.show()
     

scarti = xx_kutta-xx_eulero
visualizza_scarti = int(input('1 se si vuole visualizzare il grafico con gli scarti: '))
if (visualizza_scarti==1):
        fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)

        fig.subplots_adjust(hspace=0)
        

        # Grafico subplot 0 (dati e funzione di fit)
        ax[0].set_title('Confronto tra i due metodi', fontsize=16, color='darkred')
        ax[0].plot(tt, xx_eulero, label ='Eulero' ,c='mediumblue')
        ax[0].plot(tt, xx_kutta, label='Runge-Kutta ', c='red')
        ax[0].set_ylabel('Voltaggio(V)', fontsize=8)
        ax[0].tick_params(axis="y", labelsize=8)
        ax[0].set_xlabel('Time(s)', fontsize = 8) 
        ax[0].tick_params(axis="x", labelsize=8)
        ax[0].legend(fontsize=14, frameon=False)

        # Grafico subplot 1 (rapporto dati / funzione di fit)
        ax[1].plot(tt, scarti, c='red', label='scarti')
        ax[1].set_xlabel('Time(s)', fontsize =8)
        ax[1].set_ylabel('Scarti',  fontsize =8)
        ax[1].tick_params(axis="x",   labelsize=8) 
        ax[1].tick_params(axis="y",   labelsize=8)    
        ax[1].grid(True, axis='y')
        plt.show()


    


# definiamo ora v_in variabile nel tempo 
# array tempi 
time = np.arange(a, b, h)
# print('time', time)

# array V = 1
v = np.ones(len(time)) 
#maschera per selezionare valori interi dispari (non divisibili per 2) 
odd_mask = time.astype(int) %2 != 0
#print(odd_mask)

# assegno valori per inter dispari
v[odd_mask] = -1
print(len(v))

#print('v', v)

def fode_1(x,v_in,t):
    """funzione che definisce l'equazione differenziale"""
    return (v_in-x)/rc

xx2 = np.empty(0)
for i in range(0,len(time)):
        xx2 = np.append(xx2, x)
        k1 = h*fode_1(x,v[i],time[i])
        k2 = h*fode_1(x+0.5*k1,v[i],time[i]+0.5*h)
        k3 = h*fode_1(x+0.5*k2,v[i],time[i]+0.5*h)
        k4 = h*fode_1(x+k3,v[i],time[i]+h)
        x = x+(k1+k1*2+k3*2+k4)/6 

v_0_variabile =  int(input("1 se si vuole visualizzare l'andamento con il potenziale variabile: "))
if (v_0_variabile==1):
    
    plt.figure(figsize=[8,8])
    plt.title('Andamento della soluzione in funzione del tempo')
    plt.plot(tt, xx2)
    plt.xlabel('Time(s)')
    plt.ylabel('V_out(V)')
    plt.show()

# grafico v_in in funzione del tempo

grafico_vin = int(input('1 per visualizzare il grafico di v_in: '))
if (grafico_vin==1):
     plt.figure(figsize=[8,8])
     plt.title('Andamento di v_in in funzione del tempo: ')
     plt.plot(time, v, label ='V_in')
     plt.xlabel('Time(s)')
     plt.ylabel('V_in')
     plt.show()



prodotti = [1,0.1,0.01]
def fode_2(x,v_in,rcc,t):
    """funzione che definisce l'equazione differenziale"""
    return (v_in-x)/rcc

xsolRK4 = {}
tsolRK4 = {}

# Ciclo per diversi N
for r_c in prodotti: 
    tt = np.arange(a,b,h)
    xx3 = np.empty((0,0))

    # Ciclo per applicare iterativamente il metodo RK4 
    for i in range(0,len(time)):
        xx3 = np.append(xx3, x)
        k1 = h*fode_2(x,v[i],r_c,time[i])
        k2 = h*fode_2(x+0.5*k1,v[i],r_c,time[i]+0.5*h)
        k3 = h*fode_2(x+0.5*k2,v[i],r_c,time[i]+0.5*h)
        k4 = h*fode_2(x+k3,v[i],r_c,time[i]+h)
        x = x+(k1+k1*2+k3*2+k4)/6 
        
    # Aggiungo soluzioni ai dizionari
    xsolRK4.update({r_c : xx3})
    tsolRK4.update({r_c : tt})



# Grafico soluzioni
fig,ax = plt.subplots(figsize=(9,6))
plt.title('Metodo di Runge-Kutta al Quarto Ordine', color='slategray', fontsize=14)
for r_c in prodotti:
    plt.plot(tsolRK4[r_c],xsolRK4[r_c],label='{:.3f} RC'.format(r_c))
plt.xlabel('Time(s)')
plt.ylabel('Voltaggio(V)')
plt.legend(loc='lower right', fontsize=14)
plt.show()




# proviamo a calcolare risolvere l'equazione differenziale con scipy
xx_scipy = scipy.integrate.odeint(fode, y0=0, t=tt)
scipy_graph = int(input('1 per visualizzare il confronto tra i 3 metodi: '))
if (scipy_graph==1):
    img, ax = plt.subplots(figsize=(8,8))
    plt.title('Soluzione calcolata con scipy ')
    plt.plot(tt, xx_scipy, c='slategray', label='Scipy')
    plt.plot(tt, xx_eulero, c='mediumpurple', label='Eulero')
    plt.plot(tt, xx_kutta, c='steelblue', label='Runge Kutta')
    plt.xlabel('Time(s)')
    plt.ylabel('Voltaggio(V)')
    plt.legend(loc='lower right')
    ins = ax.inset_axes([0.45, 0.45, 0.32,0.37])
    ins.set_title('Zoom sui 3 metodi') 
    ins.plot(tt, xx_scipy, color= 'slategray',linewidth=1) 
    ins.plot(tt, xx_eulero, color= 'mediumpurple',linewidth=1)
    ins.plot(tt,xx_kutta, color= 'steelblue', linewidth=1 )
    ins.set_ylim(0.1430,0.1450)
    ins.set_xlim(0.335,0.340)
    plt.show()




















