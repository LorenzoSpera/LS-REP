import scipy 
from scipy import integrate
import pandas as pd 
import numpy
import matplotlib.pyplot as plt
import sys,os
import argparse
data = pd.read_csv('/Users/lorenzospera/Desktop/Terzo_anno/MCF/Esercitazione6/vel_vs_time.csv')
#print(data)
# salvo le velocità all'interno di una variabile v
v = data['v']

#faccio lo stesso per i tempi

t = data['t']
# plt.figure(figsize=[8,6])
# plt.title('Velocità in funzione del tempo')
# plt.plot(t , v , c='mediumblue')
# plt.ylabel('Velocità(m/s)')
# plt.xlabel('Tempo(s)')
# plt.show()

# eseguiamo ora l'integrale della velocità per ottenere lo spostamento tra due punti 

integrale = scipy.integrate.simpson(v,x=t,dx=1)
print('Il valore della posizione è: ',integrale)


distanze = []
for i in range(1,len(t)+1):
    distanze.append(scipy.integrate.simpson(v[:i],t[:i]))

# plt.title('Distanza in funzione del tempo')
# plt.plot(t, distanze, c='mediumblue')
# plt.xlabel('Tempo(s)')
# plt.ylabel('Distanza(m)')
# plt.show()



def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='esercizio1_velocità.py  --opzione')
    parser.add_argument('-f', '--opzione1',    action='store', type=str   ,help='Inserire file')
    parser.add_argument('-v', '--opzione2',    action='store_true',  help='Grafico per la velocità')
    parser.add_argument('-x', '--opzione3',    action='store_true',  help='Grafico per la legge oraria')
    return  parser.parse_args()



def pltshow():

    args = parse_arguments()

    # print 
    #print(args)

    if args.opzione2 == True:
        plt.figure(figsize=[8,6])
        plt.title('Velocità in funzione del tempo')
        plt.plot(t , v , c='mediumblue')
        plt.ylabel('Velocità(m/s)')
        plt.xlabel('Tempo(s)')
        plt.show()

    if args.opzione3 == True:
        plt.figure(figsize=[8,6])
        plt.title('Distanza in funzione del tempo')
        plt.plot(t, distanze, c='mediumblue')
        plt.xlabel('Tempo(s)')
        plt.ylabel('Distanza(m)')
        plt.show()


if __name__ == "__main__":

    pltshow()





