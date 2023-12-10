import scipy 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft, irfft
from scipy import optimize
#.fft import fft, ifft, rfft, rfftfreq, fftfreq

# leggere i tre file csv e produrre i grafici dei tre segnali 


data1 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/data_sample1.csv')
data2 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/data_sample2.csv')
data3 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/data_sample3.csv')

x1 = data1['time']
y1 = data1['meas']
x2 = data2['time']
y2 = data2['meas']
x3 = data3['time']
y3 = data3['meas']

grafici_data = int(input('1 se si vogliono visualizzare i 3 grafici dei segnali: '))
if (grafici_data==1):
    fig, ax = plt.subplots(2,2)
    fig.suptitle('Grafico dei tre segnali in funzione del tempo', c='darkred', fontsize = 12)
    ax[0][0].plot(x1, y1, label='Data 1', c='red')
    ax[0][1].plot(x2, y2, label='Data 2', c='mediumblue')
    ax[1][0].plot(x3, y3, label='Data 3', c='green')
    ax[1][1].set_visible(False)
    for i in range(0,2):
        for j in range(0,2):
            ax[i][j].set_xlabel('Time(s)')
            ax[i][j].set_ylabel('Meas(u.a)')
            ax[i][j].legend(loc='upper right')
    plt.show()
grafici_data_share_x = int(input('1 se si vogliono visualizzare i 3 grafici dei segnali che condividiono la x: '))
if (grafici_data_share_x==1):
    fig, ax = plt.subplots(3,1, sharex=True)
    fig.suptitle('Grafico dei tre segnali in funzione del tempo', c='darkred', fontsize = 12)
    ax[0].plot(x1, y1, label='Data 1', c='red')
    ax[1].plot(x2, y2, label='Data 2', c='mediumblue')
    ax[2].plot(x3, y3, label='Data 3', c='green')
    for i in range(0,3):
            ax[i].set_ylabel('Meas(u.a)')
            ax[i].legend(loc='upper right')
    ax[2].set_xlabel('Time(s)')
    plt.show()


# calcoliamo ora la trasformata dei segnali, in particolare delle y, ovvero dei punti campionati 

y1_fft = rfft(y1.values)
y2_fft = rfft(y2.values)
y3_fft = rfft(y3.values)
# definiamo l'intervallo temporale di campionamento
#  
dt=x1[1]-x1[0]
#definiamo le frequenze del segnale, per funzioni reali è necessario moltipicare le frequenz per 0.5
y1_freq = 0.5*rfftfreq(len(y1_fft), dt)
y2_freq = 0.5*rfftfreq(len(y2_fft), dt)
y3_freq = 0.5*rfftfreq(len(y3_fft), dt)

# calcoliamo ora i moduli dei coefficienti ottenuti tramite le trasformate 
y1_mod_quadro_noncut = np.abs(y1_fft)**2
y2_mod_quadro_noncut= np.abs(y2_fft)**2 
y3_mod_quadro_noncut= np.abs(y3_fft)**2 
#  questi sono quelli per fare il grafico della potenza e prendere solo le frequenze che servono
y1_mod_quadro = np.abs(y1_fft[:len(y1_fft)//2])**2
y2_mod_quadro = np.abs(y2_fft[:len(y2_fft)//2])**2 
y3_mod_quadro = np.abs(y3_fft[:len(y3_fft)//2])**2 

spettro_di_potenza = int(input('1 se si vuole visualizzare lo spettro di potenza dei 3 segnali: '))
if (spettro_di_potenza==1):
    fig, ax = plt.subplots(3,1, sharex=True, figsize =[10,8])
    fig.suptitle('Spettro di potenza dei 3 segnali', c='darkred', fontsize = 12)
    ax[0].plot(y1_freq[:len(y1_fft)//2], y1_mod_quadro, label='Data 1', c='red')
    ax[1].plot(y2_freq[:len(y2_fft)//2], y2_mod_quadro , label='Data 2', c='mediumblue')
    ax[2].plot(y3_freq[:len(y3_fft)//2], y3_mod_quadro, label='Data 3', c='green')
    for i in range(0,3):
            ax[i].set_ylabel('Potenza del segnale')
            ax[i].legend(loc='upper right')
    ax[2].set_xlabel('Frequenza(Hz)')
    plt.show()

# filtriamo il segnale scegliendo solamente dei coefficienti che abbiano un valore in potenza sopra 
# una determinata soglia
mask3 = y3_mod_quadro_noncut > 0.1e6
mask33 = y3_mod_quadro_noncut > 0.05e6
y3_fft_filtrato = y3_fft*mask3
y33_fft_filtrato = y3_fft*mask33
y3_filtrato = irfft(y3_fft_filtrato)
y33_filtrato = irfft(y33_fft_filtrato)

mask1 = y1_mod_quadro_noncut > 5e3
y1_fft_filtrato = y1_fft*mask1
y1_filtrato = irfft(y1_fft_filtrato)

mask2 = y2_mod_quadro_noncut > 100e3
mask22 = y2_mod_quadro_noncut > 50e3
y2_fft_filtrato = y2_fft*mask2
y22_fft_filtrato = y2_fft*mask22
y2_filtrato = irfft(y2_fft_filtrato)
y22_filtrato = irfft(y22_fft_filtrato)
fit_dati = int(input('1 se si voglioni visualizzare i fit dei segnali ricostruiti con diversi filtri: '))
if (fit_dati==1):
    plt.figure(figsize=[10,8])
    plt.title('Confronto tra segnale di partenza e segnale filtrato', c='darkred')
    plt.plot(x1, y1_filtrato, c='magenta', label=r'$|c_k|^2 > 5*10^3' )
    plt.plot(x1, y1 , c='gold', alpha=0.4, label='Dati di partenza')
    plt.ylabel('Meas(u.a)')
    plt.xlabel('Time(s)')
    plt.legend(loc='upper right')
    plt.show()

    plt.figure(figsize=[10,8])
    plt.title('Confronto tra segnale di partenza e segnale filtrato', c='darkred')
    plt.plot(x2, y2_filtrato, c='magenta',label=r'$|c_k|^2 > 10^5')
    plt.plot(x2, y2, c='gold', alpha=0.5, label='Dati di partenza'  )
    plt.plot(x2, y22_filtrato, c='green',label=r'$|c_k|^2 > 0.5^5' )
    plt.ylabel('Meas(u.a)')
    plt.xlabel('Time(s)')
    plt.legend(loc='upper right')
    plt.show()

    plt.figure(figsize=[10,8])
    plt.title('Confronto tra segnale di partenza e segnale filtrato', c='darkred')
    plt.plot(x3, y3_filtrato, c='green',label=r'$|c_k|^2 > 10^5')
    plt.plot(x3, y3, c='gold', alpha=0.5, label='Dati di partenza' )
    plt.plot(x3, y33_filtrato, c='magenta',label=r'$|c_k|^2 > 0.5^5' )
    plt.legend(loc='upper right')
    plt.ylabel('Meas(u.a)')
    plt.xlabel('Time(s)')
    plt.show()

def andamento(f,A,beta):
     return A/(f**beta)

pnames = ['A','beta']
pstart= [244.849,0.985]
yerr = np.full(len(y2_freq[:len(y2_fft)//2]),1)
params, params_covariance = optimize.curve_fit(andamento, y2_freq[1:len(y2_fft)//2], y2_mod_quadro[1:], sigma=yerr[1:],p0=pstart)
params_err = np.sqrt(np.diag(params_covariance))

#---------------------------------
pstart0= [4156.276,0.014]
yerr = np.full(len(y1_freq[:len(y1_fft)//2]),1)
params0, params_covariance0 = optimize.curve_fit(andamento, y1_freq[1:len(y2_fft)//2], y1_mod_quadro[1:], sigma=yerr[1:],p0=pstart0)
params_err0 = np.sqrt(np.diag(params_covariance0))
#---------------------------------
pstart3= [756.701,2]
yerr = np.full(len(y3_freq[:len(y3_fft)//2]),1)
params3, params_covariance3 = optimize.curve_fit(andamento, y3_freq[5:len(y3_fft)//2], y3_mod_quadro[5:], sigma=yerr[5:],p0=pstart3)
params_err3 = np.sqrt(np.diag(params_covariance3))
#---------------------------------

# Risultati parametri di fit
for pn, p, pe in zip(pnames, params3, params_err3):
    print('Par  {} {:>6.3f} +- {:>6.3f}'.format(pn, p, pe))
    # Risultati parametri di fit
for pn, p, pe in zip(pnames, params0, params_err0):
    print('Par  {} {:>6.3f} +- {:>6.3f}'.format(pn, p, pe))
    # Risultati parametri di fit
for pn, p, pe in zip(pnames, params, params_err):
    print('Par  {} {:>6.3f} +- {:>6.3f}'.format(pn, p, pe))

# plt.title('Grafico che riporta il plot del fit in scala logaritmica')
# plt.plot(y3_freq[5:len(y3_fft)//2], y3_mod_quadro[5:] , label='Data 3', c='mediumblue')
# plt.plot(    y3_freq[5:len(y3_fft)//2], andamento(y3_freq[5:len(y3_fft)//2], params3[0], params3[1]), label='Fit', c='red')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Log(frequenza(Hz))')
# plt.ylabel('Log(potenza(u.a))')
# plt.legend(loc='upper right')
# plt.show()
# #----------------------------------
# plt.title('Grafico che riporta il plot del fit in scala logaritmica')
# plt.plot(y2_freq[1:len(y2_fft)//2], y2_mod_quadro[1:] , label='Data 2', c='mediumblue')
# plt.plot(    y2_freq[1:len(y2_fft)//2], andamento(y2_freq[1:len(y2_fft)//2], params[0], params[1]), label='Fit', c='red')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Log(frequenza(Hz))')
# plt.ylabel('Log(potenza(u.a))')
# plt.legend(loc='upper right')
# plt.show()
# #----------------------------------
# plt.title('Grafico che riporta il plot del fit in scala logaritmica')
# plt.plot(y1_freq[1:len(y1_fft)//2], y1_mod_quadro[1:] , label='Data 1', c='mediumblue')
# plt.plot(    y1_freq[1:len(y1_fft)//2], andamento(y1_freq[1:len(y1_fft)//2], params0[0], params0[1]), label='Fit', c='red')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Log(frequenza(Hz))')
# plt.ylabel('Log(potenza(u.a))')
# plt.legend(loc='upper right')
# plt.show()


fit_dei_dati = int(input('1 se si vuole visualizzare il risultato dei fit: '))
if (fit_dei_dati==1):
    fig, ax = plt.subplots(2,2, figsize=[10,8])
    fig.suptitle('Plot dei 3 set di dati', c='darkred', fontsize =12)
    ax[0][0].plot(y1_freq[1:len(y1_fft)//2], y1_mod_quadro[1:] , label='Data 1', c='mediumblue')
    ax[0][0].plot(    y1_freq[1:len(y1_fft)//2], andamento(y1_freq[1:len(y1_fft)//2], params0[0], params0[1]), label='Fit', c='red')
    ax[1][0].plot(y2_freq[1:len(y2_fft)//2], y2_mod_quadro[1:] , label='Data 2', c='mediumblue')
    ax[1][0].plot(    y2_freq[1:len(y2_fft)//2], andamento(y2_freq[1:len(y2_fft)//2], params[0], params[1]), label='Fit', c='red')
    ax[1][1].plot(y3_freq[5:len(y3_fft)//2], y3_mod_quadro[5:] , label='Data 3', c='mediumblue')
    ax[1][1].plot(    y3_freq[5:len(y3_fft)//2], andamento(y3_freq[5:len(y3_fft)//2], params3[0], params3[1]), label='Fit', c='red')
    ax[0][1].set_visible(False)
    for i in range(0,2):
        for j in range(0,2):
            ax[i][j].set_xscale('log')
            ax[i][j].set_yscale('log')
            ax[i][j].set_xlabel('log(Frequenza(Hz))')
            ax[i][j].set_ylabel('log(Potenza(u.a))')
            ax[i][j].legend(loc='upper right')
    
    plt.show()
    





