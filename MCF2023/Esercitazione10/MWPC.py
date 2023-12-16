import pandas as pd 
import numpy as np  
import math
from numpy import random 
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt
class MWPC:
    def __init__(self, a, ncie):
        """ a rappresenta lo spessore della camera ncie è il numero 
        di coppie ione elettrone generate dopo il passaggio di una particella 
        """
        self.n_p = ncie
        self.spessore = a
    
    def passaggio_particella(self):
        """ coppie primarie è il numero di coppie generate tramite la statistica poissoniana 
        posizione è la posizione delle coppie create, distribuite con probabilità 
        uniforme lungo lo spessore """
        coppie_primarie = random.poisson(lam=self.n_p)
        posizione = np.random.uniform(low = -self.spessore/2, high=self.spessore/2, size = coppie_primarie)
        return coppie_primarie, posizione
    
    def diffusione(self,su, sf, tc, pos, nr):
        """ metodo che implementa la diffusione di elettroni 
        - su è la componente spaziale uniforme 
        - sf componente aggiuntiva lungo y per simulare l'effetto
        del campo elettrico
        - tc è il tempo medio supposto tra due urti successivi
        - nr specifica """
        x = 0
        y = pos  # posizione iniziale lungo lo spessore 
        
        distanza_minima = 0.01
        elettroni_assorbiti = np.empty(0)
        passi_totali = np.empty(0)
        tempi_di_deriva_totali = np.empty(0)
        # elettroni_assorbiti = []
        # passi_totali = []
        # tempi_di_deriva_totali = []
        for i in y:
            passi = 0
            count = 0
            while (abs(i)>distanza_minima):
                passi += 1
                """ se l'elettrone si trova nella regione sopra al filo deve spostarsi comunque 
                verso di esso e quindi il contributo costante deve essere negativa"""
                assorbimento = random.binomial(1, 1/nr)
                if (assorbimento==1):
                    elettroni_assorbiti = np.append(elettroni_assorbiti, 1)
                    count = 1
                    break

               
                angolo = np.random.uniform(low = 0, high=2*np.pi)
                if (i>0):
                    x = su*np.cos(angolo)
                    i += su*np.sin(angolo) -sf
                if (i<0):
                    x = su*np.cos(angolo)
                    i += su*np.sin(angolo) +sf
                
            passi_totali= np.append(passi_totali,passi)
            tempi_deriva = tc*passi
            if (count == 0):
                tempi_di_deriva_totali = np.append(tempi_di_deriva_totali, tempi_deriva)
            # passi_totali.append(passi)
            # print(passi_totali)
            # tempi_deriva = tc*passi
            # tempi_di_deriva_totali.append(tempi_deriva)
            
            # sono i passi di tutti gli elettroni prima di essere riassorbiti
    
        return len(elettroni_assorbiti), passi_totali, tempi_di_deriva_totali
    """len(elettroni assorbiti) restituisce il numero di elettroni assorbiti
     -passi totali restituisce un array con i passi fatti da ogni singolo elettrone assorbito
    - tempi di deriva è un array che contiene i tempi di deriva di ogni singolo elettrone assorbito """

class evento:
    def __init__(self, a, b, c, d):
        self.n_gen = a
        self.n_rive = b
        self.tempi_d = c
        self.pos_in_ril = d
camera = MWPC(1,5)  # creo un oggetto di tipo camera su cui posso richiamare i metodi    

# richiamo i metodi per vedere il numero di coppie generate e la loro posizione
#nc, pos = camera.passaggio_particella()
# print('Numero di coppie primarie generate: ', nc)
# print('Posizione lungo lo spessore delle coppie primarie: ', pos)

su = 1e-04
sf = 5e-05
nr = 1e04
tc = 1e-12

# num_assorbiti , passi_tot , tempi_der_tot = camera.diffusione(su, sf, tc, pos, nr)
# print('Il numero di elettroni riassorbiti è: ', num_assorbiti)
# print('I passi totali di ogni elettrone rilevato sono: ', passi_tot)
# print('Il tempo di deriva di ogni singolo elettrone è:', tempi_der_tot)

particelle_generate = []
particelle_rilevate = []
tempi_di_deriva = []
posizioni_coppie_iniziali = []

numero_test = int(input('Quante particelle si vogliono studiare: '))
for i in tqdm(range(numero_test)):
    nc, pos = camera.passaggio_particella()
    coppie, posizioni = camera.passaggio_particella()
    num_assorbiti , passi_tot , tempi_der_tot = camera.diffusione(su, sf, tc, pos, nr)
    particelle_generate.append(nc)
    particelle_rilevate.append(nc-num_assorbiti)
    tempi_di_deriva.append(tempi_der_tot)
    posizioni_coppie_iniziali.append(posizioni)

evento_particella = evento(particelle_generate, particelle_rilevate,tempi_di_deriva, posizioni_coppie_iniziali)
""" per calcolare il minimo tempo di deriva per evento partiamo dalla considerazione che 
un evento è costituito da un generico numero di particelle rilevate che hanno 
a loro volta un determinato tempo di deriva. tempi di deriva è una lista di array
all'interno dei quali ci sono i tempi di deriva. è necessario selezionare il minimo per ognuno 
di questi array"""

tempi_minimi = []
# facciamo la stessa cosa per le medie 
medie_tempi_deriva = []
for x in tempi_di_deriva:
    if (len(x)>0):
        min = np.min(x)
        media = np.mean(x)
        tempi_minimi.append(min)
        medie_tempi_deriva.append(media)




numero_particella = []
for i in range(numero_test):
    numero_particella.append(i)

tabella =  int(input('1 se si vuole visualizzare la tabella: '))
if (tabella==1):
    console = Console()

    # Dati delle colonne
    colonna1 = [ str(i) for i in numero_particella]
    colonna2 = [ str(i) for i in particelle_generate]
    colonna3 = [ str(i) for i in particelle_rilevate]
    #colonna4 = [ str(i) for i in tempi_di_deriva]

    # Creazione della tabella
    table = Table(title="Tabella con 4 colonne")

    # Aggiunta delle colonne
    table.add_column("Num particella", justify="center", style="cyan", no_wrap=True)
    table.add_column("Particelle generate", justify="center", style="magenta", no_wrap=True)
    table.add_column("Particelle rilevate", justify="center", style="yellow", no_wrap=True)
    #table.add_column("Tempi di deriva", justify="center", style="green", no_wrap=True)

    # Aggiunta dei dati alla tabella
    for i in range(len(numero_particella)):
        table.add_row(colonna1[i], colonna2[i], colonna3[i])

    # Stampa della tabella
    console.print(table)


# mostrare la distribuzione delle cariche rilevate 
    
generate =  int(input('1 se si vuole visualizzare la distribuzione delle cariche generate: '))
if (generate==1):
    plt.figure(figsize=[10,8])
    plt.title('Distribuzione delle particelle generate', c='darkred', fontsize = 12)
    n_gen , bins_gen, p_gen = plt.hist(particelle_generate, bins=25, color='darkblue', label='Data')
    plt.xlabel('Particelle generate')
    plt.ylabel('Eventi/bins')
    plt.legend(loc='upper right')
    plt.show()

rilevate = int(input('1 se si vuole visualizzare la distribuzione delle cariche rilevate: '))
if (rilevate==1):
    plt.figure(figsize=[10,8])
    plt.title('Distribuzione delle particelle rilevate', c='darkred', fontsize = 12)
    n_ril , bins_ril, p_ril = plt.hist(particelle_rilevate, bins=25, color='darkblue', label='Data')
    plt.xlabel('Particelle rilevate')
    plt.ylabel('Eventi/bins')
    plt.legend(loc='upper right')
    plt.show()

distribuzioni =  int(input('1 per visualizzare il grafico che riporta le distribuzioni: '))
if (distribuzioni==1):
    fig , ax = plt.subplots(2,2, figsize=[10,8])
    fig.suptitle('Distribuzione delle particelle generate e rilevate, tempi minimi e tempi medi di deriva', c='darkred', fontsize = 12)
    ax[0][0].hist(particelle_generate, bins = 25, label='Generate')
    ax[0][1].hist(particelle_rilevate, bins = 25, label='Rilevate')
    ax[1][0].hist(tempi_minimi, bins = 25, label='Tempi minimi')
    ax[1][1].hist(medie_tempi_deriva, bins = 25, label='Tempi medi')
    ax[0][0].set_xlabel('Particelle generate')
    ax[0][1].set_xlabel('Particelle rilevate')
    ax[1][0].set_xlabel('Tempi minimi')
    ax[1][1].set_xlabel('Tempi medi di deriva')
    for i in range(0,2):
        for j in range(0,2):
            ax[i][j].legend(loc='upper right')
            ax[i][j].set_ylabel('Eventi/Bins')

    plt.show()
