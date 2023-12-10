import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv("/Users/lorenzospera/Desktop/MCF_GET_DATA /get-mcf-data/4FGL_J2202.7+4216_weekly_9_11_2023.csv")

#stampo il nome delle colonne del dataframe
print(dati.columns)

#produrre il grafico del flusso in funzione del Giorno Giuliano 
"""
plt.title('Grafico del flusso dei fotoni in funzione del giorno Giuliano')
plt.plot(dati['Julian Date'],dati['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], c='royalblue')
plt.xlabel('Julian Date')
plt.ylabel('Photon Flux [0.1-100 GeV](photons cm-2 s-1)')
plt.show()

#grafico del flusso sempre in funzione del giorno Giuliano diverso, basta inserire il formato nel comando pyplot

# creare il grafico con le barre di errore con il comando errorbar

plt.errorbar(dati['Julian Date'],dati['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], yerr=dati['Photon Flux Error(photons cm-2 s-1)'] ,c = 'royalblue',fmt='o')
#per salvare il file si usa il seguente comando
plt.savefig('Grafico del flusso dei fotoni in funzione del giorno Giuliano.png')
plt.show()
"""
# produrre un grafico con asse y logaritmico 
plt.title('Grafico del flusso dei fotoni in funzione del giorno Giuliano logaritmico')
plt.errorbar(dati['Julian Date'],dati['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], yerr=dati['Photon Flux Error(photons cm-2 s-1)'] ,c = 'royalblue',fmt='o')
plt.yscale('log')
plt.xlabel('Julian Date')
plt.ylabel('Photon Flux [0.1-100 GeV](photons cm-2 s-1)')
#per salvare il file si usa il seguente comando
plt.savefig('Grafico del flusso dei fotoni in funzione del giorno Giuliano log.png')
plt.show()