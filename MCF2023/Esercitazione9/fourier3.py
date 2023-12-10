import scipy 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft, irfft
from scipy import optimize
plt.rcParams['axes.facecolor'] = 'beige'

# leggere i dati dal file copernicus 

data = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/copernicus_PG_selected.csv')
print('Colonne:', data.columns)

co = data['mean_co_ug/m3']
nh3 = data['mean_nh3_ug/m3']
no2 = data['mean_no2_ug/m3']
o3 = data['mean_o3_ug/m3']
pm10 = data['mean_pm10_ug/m3']
pm2p5 = data['mean_pm2p5_ug/m3']
so2 = data['mean_so2_ug/m3']

date_old = data['date_old']
date = data['date']


grafico_conc = int(input('1 se si vuole visualizzare la concentrazione degli inquinanti nel tempo: '))
if (grafico_conc==1):
    plt.figure(figsize=[10,8])
    plt.title('Concentrazioni in funzione di date old ')
    plt.plot(date_old, co, label='co', c='red')
    plt.plot(date_old, nh3, label='nh3', c='blue')
    plt.plot(date_old, no2,label='no2', c='limegreen')
    plt.plot(date_old, o3,label='o3',c='purple')
    plt.plot(date_old, pm10,label='pm10',c='gold')
    plt.plot(date_old, pm2p5,label='pm2p5',c='deepskyblue',)
    plt.plot(date_old, so2,label='so2', c='black')
    plt.legend(loc='upper right')
    plt.xlabel('Data')
    plt.ylabel('Concetrazione(u.a)')
    plt.show()

grafico_date = int(input('1 se si vuole visualizzare la concentrazione degli inquinanti nel tempo: '))
if (grafico_date==1):
    fig = plt.figure(figsize=[10,8])
    fig.patch.set_facecolor('gray')
    plt.title('Concentrazioni in funzione di date old ')
    plt.plot(date, co, label='co', c='red')
    plt.plot(date, nh3, label='nh3', c='blue')
    plt.plot(date, no2,label='no2', c='limegreen')
    plt.plot(date, o3,label='o3',c='purple')
    plt.plot(date, pm10,label='pm10',c='gold')
    plt.plot(date, pm2p5,label='pm2p5',c='deepskyblue',)
    plt.plot(date, so2,label='so2', c='cyan')
    plt.legend(loc='upper right')
    plt.xlabel('Data')
    plt.ylabel('Concetrazione(u.a)')
    plt.show()


# trasformate di fourier della serie temporale della co 
dt = date[3]-date[2]
co_fft = rfft(co.values)
co_fft_im = fft(co.values)
co_freq = 0.5*rfftfreq(len(co_fft), dt)
co_freq_re = fftfreq(len(co_fft), dt)
co_potenza = (np.abs(co_fft[:len(co_fft)//2]))**2
co_potenza_noncut = (np.abs(co_fft))**2

spettro_potenza = int(input('1 se si vuole visualizzare lo spettro di potenza della co non il log: '))
if (spettro_potenza==1):
    plt.figure(figsize=[10,8])
    plt.title('Spetrro di potenza in funzione della frequenza ')
    plt.plot(co_freq[:len(co_fft)//2], co_potenza, label='Potenza', c='coral')
    plt.legend(loc='upper right')
    plt.xlabel('Frequenza(u.a)')
    plt.ylabel('Potenza(u.a)')
    plt.show()

spettro_potenza = int(input('1 se si vuole visualizzare lo spettro di potenza della co: '))
if (spettro_potenza==1):
    plt.figure(figsize=[10,8])
    plt.title('Spetrro di potenza in funzione della frequenza ')
    plt.plot(co_freq[:len(co_fft)//2], co_potenza, label='Potenza', c='coral')
    plt.legend(loc='upper right')
    plt.xlabel('Frequenza(u.a)')
    plt.ylabel('Potenza(u.a)')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


# la periodicità è un anno 

periodi = 1/(co_freq[1:len(co_fft)//2])
spettro_periodi = int(input('1 se si vuole visualizzare lo spettro di potenza in funzione del periodo: '))
if (spettro_periodi==1):
    plt.figure(figsize=[10,8])
    plt.title('Spettro in funzione del periodo ')
    plt.plot(periodi, co_potenza[1:], label='Potenza', c='coral')
    plt.legend(loc='upper right')
    plt.xlabel('Periodo(u.a)')
    plt.ylabel('Potenza(u.a)')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()



# il segnale e confrontarlo con quello di partenza 
maschera_co = co_potenza_noncut>0.2e6
co_fft_filtrata = co_fft*maschera_co
co_filtrato = irfft(co_fft_filtrata)
maschera_co1 = co_potenza_noncut>5e6
maschera_co2 = co_potenza_noncut>1e7
maschera_co3 = co_potenza_noncut>5e8
co_fft_filtrata1 = co_fft*maschera_co1
co_fft_filtrata2 = co_fft*maschera_co2
co_fft_filtrata3 = co_fft*maschera_co3
co_filtrato1 = irfft(co_fft_filtrata1)
co_filtrato2 = irfft(co_fft_filtrata2)
co_filtrato3 = irfft(co_fft_filtrata3)

ricosturuzione = int(input('1 se si vuole visualizzare la ricostruzione con diverse maschere: '))
if (ricosturuzione==1):
    fig , ax = plt.subplots(2,2, figsize=[10,8])
    ax[0][0].plot(date, co, label='co', c='red')
    ax[0][0].plot(date, co_filtrato, label=r'|c_k|^2>0.2e6', c='blue' )
    ax[1][0].plot(date, co, label='co', c='red')
    ax[1][0].plot(date, co_filtrato1, label=r'|c_k|^2>5e6', c='blue' )
    ax[1][1].plot(date, co, label='co', c='red')
    ax[1][1].plot(date, co_filtrato2, label=r'|c_k|^2>1e7', c='blue' )
    ax[0][1].plot(date, co, label='co', c='red')
    ax[0][1].plot(date, co_filtrato3, label=r'|c_k|^2>5e8', c='blue' )
    for i in range(0,2):
        for j in range(0,2):
            ax[i][j].legend(loc='upper right')
    for i in range(0,2):
        for j in range(0,2):
            ax[i][j].set_xlabel('Time(u.a)')
            ax[i][j].set_xlabel('Concentrazione(u.a)')
    plt.show()


print(len(co_freq))
print(len(co_freq_re))
