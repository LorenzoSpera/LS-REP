import scipy 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft, irfft
from scipy import optimize


data1 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv')
data2 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/4FGL_J0721.9+7120_weekly_9_15_2023_mcf.csv')
data3 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
data4 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv')
data5 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/4FGL_J2232.6+1143_weekly_9_15_2023_mcf.csv')
data6 = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/MCF_GET_DATA /get-mcf-data/es_fourier/4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv')
julian_date1 = data1['Julian Date']
julian_date2 = data2['Julian Date']
julian_date3 = data3['Julian Date']
julian_date4 = data4['Julian Date']
julian_date5 = data5['Julian Date']
julian_date6 = data6['Julian Date']


# generare un grafico con tutte le curve di luce in funzione del giorno giuliano, tutte sovrapposte

print(data1.columns)
confronto_curve_1 = int(input('1 se si vuole visualizzare la sovrapposizione delle 6 curve di luce: '))
if (confronto_curve_1==1):
    plt.figure(figsize=[10,8])
    plt.title('Confronto tra le sei curve di luce sovrapposte tra di loro specificandone la sorgente e il tipo', c='darkred', fontsize= 12)
    plt.plot(data1['Julian Date'], data1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='limegreen', label='sorgente PKS 0426-380 , classe BLL')
    plt.plot(data2['Julian Date'], data2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='red',label='sorgente S5 0716+71 , classe BLL')
    plt.plot(data3['Julian Date'], data3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='blue',label='sorgente 3C 279 , classe FSRQ ')
    plt.plot(data4['Julian Date'], data4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='purple', label=' sorgente Bl Lac , classe BLL')
    plt.plot(data5['Julian Date'], data5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='gold',label=' sorgente CTA 102 , classe FSRQ')
    plt.plot(data6['Julian Date'], data6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='deepskyblue',label='sorgente 3C 454.3 , classe FSRQ')
    plt.xlabel('Giorno giuliano')
    plt.ylabel('Fluso di fotoni (cm-2 s-1)')
    plt.legend(loc='upper right')
    plt.show()


grafici_singoli = int(input('1 se si voglioni visualizzare i grafici delle due classi: '))
if (grafici_singoli==1):
    fig, ax = plt.subplots(3,2, figsize=[10,8], sharex=True)
    fig.suptitle('Confronto delle curve di luce in base alla classe')
    ax[0][0].set_title('Grafico curve di luce BBL')
    ax[0][1].set_title('Grafico curve di luce FSRQ')
    ax[0][0].plot(data1['Julian Date'], data1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='limegreen', label='sorgente PKS 0426-380 , classe BLL')
    ax[1][0].plot(data2['Julian Date'], data2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='limegreen', label='sorgente S5 0716+71 , classe BLL')
    ax[2][0].plot(data4['Julian Date'], data4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='limegreen', label=' sorgente Bl Lac , classe BLL')
    ax[0][1].plot(data3['Julian Date'], data3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='deepskyblue', label='sorgente 3C 279 , classe FSRQ ')
    ax[1][1].plot(data5['Julian Date'], data5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='deepskyblue', label=' sorgente CTA 102 , classe FSRQ')
    ax[2][1].plot(data6['Julian Date'], data6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='deepskyblue', label='sorgente 3C 454.3 , classe FSRQ')
    for i in range(0,3):
        for j in range(0,2):
            ax[i][j].legend(loc='upper right')
    ax[2][0].set_xlabel('Giorno giuliano')
    ax[2][1].set_xlabel('Giorno giuliano')
    for i in range(0,3):
        for j in range(0,2):
            ax[i][j].set_ylabel('Photon Flux')
    plt.show()


# calcolare le fft delle curve di luce 
fft1 = fft(data1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft2 = fft(data2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft3 = fft(data3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft4 = fft(data4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft5 = fft(data5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft6 = fft(data6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
dt1 = julian_date1[3]-julian_date1[2]
dt2 = julian_date2[3]-julian_date2[2]
dt3 = julian_date3[3]-julian_date3[2]
dt4 = julian_date4[3]-julian_date4[2]
dt5 = julian_date5[3]-julian_date5[2]
dt6 = julian_date6[3]-julian_date6[2]
freq1 = 0.5*rfftfreq(len(fft1), dt1)
freq2 = 0.5*rfftfreq(len(fft2), dt2)
freq3 = 0.5*rfftfreq(len(fft3), dt3)
freq4 = 0.5*rfftfreq(len(fft4), dt4)
freq5 = 0.5*rfftfreq(len(fft5), dt5)
freq6 = 0.5*rfftfreq(len(fft6), dt6)


# calcoliamo ora i moduli dei coefficienti ottenuti tramite le trasformate 
y1_mod_quadro_noncut = np.abs(fft1)**2
y2_mod_quadro_noncut= np.abs(fft2)**2 
y3_mod_quadro_noncut= np.abs(fft3)**2 
y4_mod_quadro_noncut = np.abs(fft4)**2
y5_mod_quadro_noncut= np.abs(fft5)**2 
y6_mod_quadro_noncut= np.abs(fft6)**2 
#  questi sono quelli per fare il grafico della potenza e prendere solo le frequenze che servono
y1_mod_quadro = np.abs(fft1[:len(fft1)//2])**2
y2_mod_quadro = np.abs(fft2[:len(fft2)//2])**2 
y3_mod_quadro = np.abs(fft3[:len(fft3)//2])**2 
y4_mod_quadro = np.abs(fft4[:len(fft4)//2])**2
y5_mod_quadro = np.abs(fft5[:len(fft5)//2])**2 
y6_mod_quadro = np.abs(fft6[:len(fft6)//2])**2 

confronto_spettro = int(input('1 se si vuole visualizzare la sovrapposizione dei 6 spettri '))
if (confronto_spettro==1):
    plt.figure(figsize=[10,8])
    plt.title('Confronto tra i 6 spettri in potenza tra di loro specificandone la sorgente e il tipo', c='darkred', fontsize= 12)
    plt.plot(freq1[:-1], y1_mod_quadro, c='limegreen', label='classe BLL' )
    plt.plot(freq2[:-1], y2_mod_quadro, c='limegreen')
    plt.plot(freq4[:-1], y4_mod_quadro, c='limegreen' )
    plt.plot(freq3[:-1], y3_mod_quadro, c='deepskyblue', label=' classe FSRQ ' )
    plt.plot(freq5[:-1], y5_mod_quadro, c='deepskyblue')
    plt.plot(freq6[:-1], y6_mod_quadro, c='deepskyblue')
    plt.xlabel('Frequenza')
    plt.ylabel('Potenza(u.a)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.show()

confronto_spettro_plo_diversi = int(input('1 se si vuole visualizzare i 6 spettri su plot diversi: '))
if (confronto_spettro_plo_diversi==1):
    fig, ax  = plt.subplots(3,2, figsize =[10,8])
    fig.suptitle('Spettro di potenza delle due classi in plot separati', c='darkred', fontsize = 12)
    ax[0][0].plot(freq1[:-1], y1_mod_quadro, c='limegreen', label='sorgente PKS 0426-380 , classe BLL')
    ax[1][0].plot(freq2[:-1], y2_mod_quadro, c='limegreen', label='sorgente S5 0716+71 , classe BLL')
    ax[2][0].plot(freq3[:-1], y3_mod_quadro, c='limegreen', label=' sorgente Bl Lac , classe BLL' )
    ax[0][1].plot(freq4[:-1], y4_mod_quadro, c='deepskyblue',label='sorgente 3C 279 , classe FSRQ ' )
    ax[1][1].plot(freq5[:-1], y5_mod_quadro, c='deepskyblue', label=' sorgente CTA 102 , classe FSRQ')
    ax[2][1].plot(freq6[:-1], y6_mod_quadro, c='deepskyblue', label='sorgente 3C 454.3 , classe FSRQ')
    ax[2][0].set_xlabel('Frequenza(u.a)')
    ax[2][1].set_xlabel('Frequenza(u.a)')
    for i in range(0,3):
        for j in range(0,2):
            ax[i][j].set_ylabel('Potenza(u.a)')
    for i in range(0,3):
        for j in range(0,2):
            ax[i][j].legend(loc='upper right')
            ax[i][j].set_xscale('log')
            ax[i][j].set_yscale('log')
    plt.show()


# spettri in potenza normalizzati
potenza1_norm = np.abs(fft1[:len(fft1)//2]/fft1[0])**2
potenza2_norm = np.abs(fft2[:len(fft2)//2]/fft2[0])**2
potenza3_norm = np.abs(fft3[:len(fft3)//2]/fft3[0])**2
potenza4_norm = np.abs(fft4[:len(fft4)//2]/fft4[0])**2
potenza5_norm = np.abs(fft5[:len(fft5)//2]/fft5[0])**2
potenza6_norm = np.abs(fft6[:len(fft6)//2]/fft6[0])**2

confronto_norm = int(input('1 se si vuole visualizzare la sovrapposizione dei 6 spettri normalizzati '))
if (confronto_norm==1):
    plt.figure(figsize=[10,8])
    plt.title('Confronto tra i 6 spettri normalizzati in potenza tra di loro specificandone la sorgente e il tipo', c='darkred', fontsize= 12)
    plt.plot(freq1[:-1], potenza1_norm, c='limegreen', label='classe BLL' )
    plt.plot(freq2[:-1], potenza2_norm, c='limegreen')
    plt.plot(freq4[:-1], potenza4_norm, c='limegreen' )
    plt.plot(freq3[:-1], potenza3_norm, c='deepskyblue', label=' classe FSRQ ' )
    plt.plot(freq5[:-1], potenza5_norm, c='deepskyblue')
    plt.plot(freq6[:-1], potenza6_norm, c='deepskyblue')
    plt.xlabel('Frequenza')
    plt.ylabel('Potenza(u.a)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.show()

confronto_norm_nonlog = int(input('1 se si vuole visualizzare la sovrapposizione dei 6 spettri normalizzati '))
if (confronto_norm_nonlog==1):
    plt.figure(figsize=[10,8])
    plt.title('Confronto tra i 6 spettri normalizzati in potenza tra di loro specificandone la sorgente e il tipo', c='darkred', fontsize= 12)
    plt.plot(freq1[:-1], potenza1_norm, c='limegreen', label='classe BLL' )
    plt.plot(freq2[:-1], potenza2_norm, c='limegreen')
    plt.plot(freq4[:-1], potenza4_norm, c='limegreen' )
    plt.plot(freq3[:-1], potenza3_norm, c='deepskyblue', label=' classe FSRQ ' )
    plt.plot(freq5[:-1], potenza5_norm, c='deepskyblue')
    plt.plot(freq6[:-1], potenza6_norm, c='deepskyblue')
    plt.xlabel('Frequenza')
    plt.ylabel('Potenza(u.a)')
    plt.legend(loc='upper right')
    plt.show()
confronto_spettro_plot_normalizzati = int(input('1 se si vuole visualizzare i 6 spettri normalizzati su plot diversi: '))
if (confronto_spettro_plot_normalizzati==1):
    fig, ax  = plt.subplots(3,2, figsize =[10,8])
    fig.suptitle('Spettro di potenza normalizzati delle due classi in plot separati', c='darkred', fontsize = 12)
    ax[0][0].plot(freq1[:-1], potenza1_norm, c='limegreen', label='sorgente PKS 0426-380 , classe BLL')
    ax[1][0].plot(freq2[:-1], potenza2_norm, c='limegreen', label='sorgente S5 0716+71 , classe BLL')
    ax[2][0].plot(freq3[:-1], potenza3_norm, c='limegreen', label=' sorgente Bl Lac , classe BLL' )
    ax[0][1].plot(freq4[:-1], potenza4_norm, c='deepskyblue',label='sorgente 3C 279 , classe FSRQ ' )
    ax[1][1].plot(freq5[:-1], potenza5_norm, c='deepskyblue', label=' sorgente CTA 102 , classe FSRQ')
    ax[2][1].plot(freq6[:-1], potenza6_norm,c='deepskyblue', label='sorgente 3C 454.3 , classe FSRQ')
    ax[2][0].set_xlabel('Frequenza(u.a)')
    ax[2][1].set_xlabel('Frequenza(u.a)')
    for i in range(0,3):
        for j in range(0,2):
            ax[i][j].set_ylabel('Potenza(u.a)')
    for i in range(0,3):
        for j in range(0,2):
            ax[i][j].legend(loc='upper right')
            ax[i][j].set_xscale('log')
            ax[i][j].set_yscale('log')
    plt.show()