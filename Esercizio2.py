import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#creo il data-frame leggendo i dati da file 
dati = pd.read_csv("/Users/lorenzospera/Desktop/MCF_GET_DATA /get-mcf-data/4LAC_DR2_sel.csv")

#stampo il nome delle colonne del dataframe
print(dati.columns)

#stampo un estratto del contenuto 
print(dati.iloc[5:10])

#produrre un grafico dell'idice spettrale in funzione del flusso flux1000
plt.title('Grafico del flusso in funzione dell indice spettrale')
plt.scatter(dati['Flux1000'],dati['PL_Index'],c='royalblue')
plt.xlabel('Indice spettrale')
plt.ylabel('Flusso')
#plt.show()

# grafico con assex logaritmico
plt.title('Grafico del flusso in funzione dell indice spettrale')
plt.scatter(dati['Flux1000'],dati['PL_Index'],c='royalblue')
plt.xlabel('Indice spettrale')
plt.ylabel('Flusso')
plt.xscale('log')
#plt.show()

#produca un grafico dell'indice spettrale (PL_Index) in funzione del logaritmo in base 10 della variabile nu_syn
# dato che si sono valori che sono nulli non si può estrarre il logaritmo, quindi è necessario applicare una maschera e filtrare
# i valori necessari

dati1 = dati.loc[( dati['nu_syn'] > 0)]
plt.title('Grafico del flusso in funzione della variabile nu_syn')
plt.scatter(dati1['nu_syn'],dati1['PL_Index'],c='royalblue')
plt.xlabel('Indice spettrale')
plt.ylabel('Flusso')
plt.xscale('log')
#plt.show()

"""produca un grafico dell'indice spettrale (PL_Index) in funzione del logaritmo in base 10 della variabile nu_syn distinguendo le sorgenti di classe (CLASS) bll e fsrq con la corrispondente legenda (gli altri tipi di sorgente non vanno considerate nel grafico);
suggerimento: usare .loc per la serezione dei valori nel DataFrame;
suggerimento: usare l'opzione alpha per la trasparenza;"""

dati_bll = dati1.loc[(dati1['CLASS'])=='bll']
dati_fsrq = dati1.loc[(dati1['CLASS'])=='fsrq']
plt.title('Grafico con le due sorgenti diverse')
plt.scatter(dati_fsrq['nu_syn'],dati_fsrq['PL_Index'],c='red',alpha=0.4,label='frsq')
plt.scatter(dati_bll['nu_syn'],dati_bll['PL_Index'],c='grey',alpha=0.2,label='bll')
plt.xlabel('nu_syn')
plt.ylabel('Pl_index')
plt.xscale('log')
plt.legend()
#plt.show()

"""produca un grafico analogo a quello del punto 7 ma che mostri anche l'incertezza sulla stima dell'indice spettrale (Unc_PL_Index);
suggerimento: usare pyplot.errorbar;"""

dati_bll = dati1.loc[(dati1['CLASS'])=='bll']
dati_fsrq = dati1.loc[(dati1['CLASS'])=='fsrq']
plt.title('Grafico con le due sorgenti diverse')
plt.errorbar(dati_fsrq['nu_syn'],dati_fsrq['PL_Index'],yerr=dati_fsrq['Unc_PL_Index'],c='red',alpha=0.4,label='frsq')
plt.errorbar(dati_bll['nu_syn'],dati_bll['PL_Index'],yerr=dati_bll['Unc_PL_Index'],c='grey',alpha=0.2,label='bll')
plt.xlabel('Nu_syn')
plt.ylabel('PL_index')
plt.xscale('log')
plt.legend()
#plt.show()

# produrre ora un istogramma per le due sorgenti con lo stesso numero di bin 

n_bll, bins_bll, p_bll = plt.hist(np.log10(dati_bll['PL_Index']),bins = 200, range=(0,0.8),color='limegreen',label='FSRQ',alpha=0.3)
n_fsrq, bins_fsrq ,p_fsrq =plt.hist(np.log10(dati_fsrq['PL_Index']),bins = 200, range=(0,0.8),color='grey',label='BLL',alpha=0.3)

plt.legend()
#plt.show()

# utilizzo di pyplots 
fig = plt.figure()

gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
ax2.set_visible(False)
fig.suptitle('Sharing x per column, y per row')
ax1.hist(np.log10((dati_fsrq['nu_syn'])),bins = 200, range=(10,20),color='grey',label='FSRQ',alpha=0.3)
ax1.hist(np.log10((dati_bll['nu_syn'])),bins = 200, range=(10,20),color='red',label='BLL',alpha=0.3)
ax1.set_ylabel('Number of sources')
ax3.scatter(np.log10(dati_fsrq['nu_syn']),dati_fsrq['PL_Index'],c='red',alpha=0.3,label='frsq')
ax3.scatter(np.log10(dati_bll['nu_syn']),dati_bll['PL_Index'],c='grey',alpha=0.3,label='bll')
ax3.set_xlabel('Logaritmo nu sin')
ax3.set_ylabel('PL_Index')
ax4.hist((dati_fsrq['PL_Index']),bins = 200, range=(1,3.5),color='grey',label='FSRQ',alpha=0.3,orientation='horizontal')
ax4.hist((dati_bll['PL_Index']),bins = 200, range=(1,3.5),color='red',label='BLL',alpha=0.3,orientation='horizontal')
ax4.set_xlabel('Number of sources')

#for ax in fig.get_axes():
    #ax.label_outer()
plt.show()
