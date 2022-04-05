"""sito eratostenesa liczby"""

from math import *

#Robi to samo co sito reatostenesa-True-list ale tu od początku mamy listę z cyframi

a = int(input("Podaj liczbę do której będziemy wyznaczać: "))
tablica = []

for b in range(2, a+1):
    tablica.append(b)

for i in range(2, int(sqrt(a))):    #iterujemy przez tablicę 
    if i in tablica:    #jeśli 'i' znajduje się w tablicy to ...
        for j in range(i*i, a+1, i):    #dla wsystkich 'j'               w tablicy usuwamy wielokotności 'i'
            if j in tablica:                              #występujących
                tablica.remove(j)

print("Liczbami pierwszymi z tego przedziału od 2 do", a, "są: \n",tablica)

            
