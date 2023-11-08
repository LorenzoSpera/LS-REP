import sys
import somme

sys.path.append('somme.py')
sys.path

n = int(input('Inserire i numeri naturali di cui si vuole calcolare la somma e prodotto '))
somma , prodotto = somme.somma_e_prodotto(n)
somma1 = somme.somma_numeri(n)
somma_radici1 = somme.somma_radici(n)
print ('Somma prima metodo: ', somma1)
print('Somma radici: ', somma_radici1)
print('Somma: ', somma)
print('Prodotto:', prodotto)
somma_alpha = somme.somma_alpha(n)
print('Somma numeri:', somma_alpha)