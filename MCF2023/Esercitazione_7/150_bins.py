import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt 
import scipy 
from scipy import optimize

data = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/Esercizi_svolti_da_me/Esercitazione_7/Jpsimumu.csv')

eventi = np.array(data['Event'])
energia1 = np.array(data['E1'])
energia2 = np.array(data['E2'])
p1x = np.array(data['px1'])
p1y = np.array(data['py1'])
p1z = np.array(data['pz1'])
p2x = np.array(data['px2'])
p2y = np.array(data['py2'])
p2z = np.array(data['pz2'])

somma_energie_quadre = pow(energia1+energia2,2)
somma_momenti_x = pow(p1x+p2x, 2)
somma_momenti_y = pow(p1y+p2y, 2)
somma_momenti_z = pow(p1z+p2z, 2)
massa_invariante = np.sqrt(somma_energie_quadre-(somma_momenti_x+somma_momenti_y+somma_momenti_z))



    # distribuzione delle masse 

fig,ax = plt.subplots(figsize=(10,7))
plt.title('Distribuzione della massa invariante')
n, bins, p = plt.hist(massa_invariante, bins=150, color='mediumblue', label='Massa invariante')

ins = ax.inset_axes([0.6, 0.5, 0.3,0.3]) # i primi due parametri sono le coordinate, i secondi due le scale 
ins.set_title('Intervallo attorno al picco')
n1, bins1, p1 = ins.hist(massa_invariante, bins=150, range=(3,3.25), color='mediumblue')
plt.legend(loc='upper right') 
plt.show()

# fit con gaussiana singola 
def gaussiana1(x, A, m, p1, p0, sigma):
    return A*np.exp(-((x-m)**2)/(2*sigma**2))+p1*x+p0
def gaussiana2(x, A1, A2, m, p1, p0, sigma1, sigma2):
        return A1*np.exp(-((x-m)**2)/(2*sigma1**2))+A2*np.exp(-((x-m)**2)/(2*sigma2**2))+p1*x+p0

# definiamo la maschera per selezionare le masse nel range 
maschera = np.logical_and(massa_invariante>3, massa_invariante<3.2)

massa_filtrata = massa_invariante[maschera]
x = massa_filtrata



plt.title('Andamento intorno al picco')
n2, bins2, p2 = plt.hist(x, bins=150, color='mediumblue')
bincenters = (bins2[:-1] + bins2[1:])/2
plt.show()
print(n2)
print(bincenters)






# # Fit per trovare parametri
pstart = np.array([1.54854274e+02, 3.09317519, -3.24627733e+01, 1.15295086e+02,  2.63408913e-02])
params, params_covariance = optimize.curve_fit(gaussiana1, xdata=bincenters, ydata=n2, p0=[pstart])


print('params', params )
print('params_cov', params_covariance)
print('errori params', np.sqrt(params_covariance.diagonal()))
scelta_gaussiana1 = int(input('1 per visualizzare fir prima gaussiana: '))
if (scelta_gaussiana1==1):

    n2, bins2, p2 = plt.hist(x, bins=150, color='blue')
    plt.title('Fit dei dati intorno al picco con prima gaussiana')
    plt.plot(bincenters, gaussiana1(bincenters, params[0],params[1],params[2],params[3],params[4]),'o', c='darkred',label='Fit con gaussiana 1')
    plt.xlabel('X')
    plt.ylabel('Eventi / Bin')
    plt.legend(loc='upper right')
    plt.show()

        # fit con seconda gaussiana 

    
pstart1 = np.array([1.54854274e+02,1.54854274e+02, 3.09317519, -3.24627733e+01, 1.15295086e+02,  2.63408913e-02,2.63408913e-02])
params1, params_covariance1 = optimize.curve_fit(gaussiana2, xdata=bincenters, ydata=n2, p0=[pstart1])

print('params', params )
print('params_cov', params_covariance)
print('errori params', np.sqrt(params_covariance.diagonal()))

scelta_gaussiana2 = int(input('1 per visualizzare fir con gaussiana 2: '))
if (scelta_gaussiana2==1):
    
  
    plt.title('Fit dei dati intorno al picco con seconda gaussiana')
    n3, bins3, p3 = plt.hist(x, bins=150, color='mediumblue')
    plt.plot(bincenters, gaussiana2(bincenters, params1[0],params1[1],params1[2],params1[3],params1[4],params1[5],params1[6]),'o', c='limegreen',label='Fit con seconda gaussiana 2' )
    plt.legend(loc='upper right')
    plt.xlabel('X')
    plt.ylabel('Eventi / Bin')
    plt.show()


# calcolo del chi quadro 
# Calcolo Chi quadrato
# Valore funzine fit ottimizzata in corrispondneza dei tempi dei dati
yfit_gaussiana1 = gaussiana1(bincenters, params[0],params[1],params[2],params[3],params[4])
ydata_gaussiana1 = n2 
# chi2
chi2_gaussiana1 =  np.sum( (yfit_gaussiana1 - ydata_gaussiana1)**2 /ydata_gaussiana1 ) 

# gradi di libertà
ndof_gaussiana1 = len(bincenters)-len(params)
print('Il chi quadrato calcolato con la prima gaussiana è data da ')
print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2_gaussiana1, ndof_gaussiana1, chi2_gaussiana1/ndof_gaussiana1 ) )
yfit_gaussiana2 = gaussiana2(bincenters,params1[0],params1[1],params1[2],params1[3],params1[4],params1[5],params1[6])
ydata_gaussiana2 = n2 
# chi2
chi2_gaussiana2 =  np.sum( (yfit_gaussiana2 - ydata_gaussiana2)**2 /ydata_gaussiana2 ) 

# gradi di libertà
ndof_gaussiana2 = len(bincenters)-len(params1)

print('Il chi quadrato ottenuto con la seconda gaussiana è dato da ')
print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2_gaussiana2, ndof_gaussiana2, chi2_gaussiana2/ndof_gaussiana2) )


# confronto dei dati con i fit

##############################################
# Grafico con Rapporto Dati/Fit
##############################################

scelta_fit = int(input('1 per visualizzare il confronto tra i dati e il fit: '))

if (scelta_fit==1):
    # Grafico con due subplot
    fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
    # Rimuovo spazio verticale fra i subplot
    fig.subplots_adjust(hspace=0)
    fig.suptitle('Confronto dati con fit per la prima gaussiana')

    # Grafico subplot 0 (dati e funzione di fit)
    ax[0].set_title('Fit gaussiana 1', fontsize=16, color='darkred')
    ax[0].errorbar(bincenters,  n2,  color='royalblue', fmt='o', label='Dati')
    ax[0].plot(    bincenters, gaussiana1(bincenters, params[0],params[1],params[2],params[3],params[4]),color='darkorange')
    ax[0].set_ylabel('Eventi Misurati', fontsize=14)
    ax[0].tick_params(axis="y", labelsize=14) 
    ax[0].legend(fontsize=14, frameon=False)
    ax[0].text(0, min(n2), r'$\chi^2$ / ndf : {:3.2f} / {:d}'.format(chi2_gaussiana1, ndof_gaussiana1), fontsize=16, color='dimgray')

    # Grafico subplot 1 (rapporto dati / funzione di fit)
    ax[1].errorbar(bincenters,  ydata_gaussiana1/yfit_gaussiana1, fmt='o', color='royalblue' )
    ax[1].axhline(1, color='darkorange') 
    ax[1].set_xlabel('Massa invariante (u.a)', fontsize =14)
    ax[1].set_ylabel('Dati/Fit',  fontsize =14)
    ax[1].tick_params(axis="x",   labelsize=14) 
    ax[1].tick_params(axis="y",   labelsize=14) 
    ax[1].set_ylim(0.5,1.5)       
    ax[1].set_yticks(np.arange(0.5, 1.51, 0.25))
    ax[1].grid(True, axis='y')
    # Salvo immagine grafico come file .png e .pdf 
    #plt.savefig('exponential_fit.png')
    #plt.savefig('exponential_fit.pdf')
    plt.show()


    # facciamo lo stesso per la seconda gaussiana

    fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
    # Rimuovo spazio verticale fra i subplot
    fig.subplots_adjust(hspace=0)
    fig.suptitle('Confronto dati/fit per le due gaussiane')

    # Grafico subplot 0 (dati e funzione di fit)
    ax[0].set_title('Fit con gaussiana 2', fontsize=16, color='darkred')
    ax[0].errorbar(bincenters,  n2,  color='royalblue', fmt='o', label='Dati')
    ax[0].plot(    bincenters, gaussiana2(bincenters, params1[0],params1[1],params1[2],params1[3],params1[4],params1[5],params1[6]),color='darkorange')
    ax[0].set_ylabel('Eventi Misurati', fontsize=14)
    ax[0].tick_params(axis="y", labelsize=14) 
    ax[0].legend(fontsize=14, frameon=False)
    ax[0].text(0, min(n2), r'$\chi^2$ / ndf : {:3.2f} / {:d}'.format(chi2_gaussiana2, ndof_gaussiana2), fontsize=16, color='dimgray')

    # Grafico subplot 1 (rapporto dati / funzione di fit)
    ax[1].errorbar(bincenters,  ydata_gaussiana2/yfit_gaussiana2, fmt='o', color='royalblue' )
    ax[1].axhline(1, color='darkorange') 
    ax[1].set_xlabel('Massa invariante(u.a)', fontsize =14)
    ax[1].set_ylabel('Dati/Fit',  fontsize =14)
    ax[1].tick_params(axis="x",   labelsize=14) 
    ax[1].tick_params(axis="y",   labelsize=14) 
    ax[1].set_ylim(0.5,1.5)       
    ax[1].set_yticks(np.arange(0.5, 1.51, 0.25))
    ax[1].grid(True, axis='y')
    # Salvo immagine grafico come file .png e .pdf 
    #plt.savefig('exponential_fit.png')
    #plt.savefig('exponential_fit.pdf')
    plt.show()