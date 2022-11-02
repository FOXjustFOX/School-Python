"""sito eratostenesa liczby"""

import time

#Robi to samo co sito reatostenesa-True-list ale tu od początku mamy listę z cyframi

a = int(input("Podaj liczbę do której będziemy wyznaczać: "))
tablica = []

t0 = time.time()
for b in range(2, a+1):
    tablica.append(b)

t1 = time.time()

for i in range(2, int(a**(1/2))):    #iterujemy przez tablicę 
    if i in tablica:    #jeśli 'i' znajduje się w tablicy to ...
        for j in range(i*i, a+1, i):    #dla wsystkich 'j'               w tablicy usuwamy wielokotności 'i'
            if j in tablica:                              #występujących
                tablica.remove(j)


print("Liczbami pierwszymi z tego przedziału od 2 do", a, "są: \n",tablica)
print('time:', t1 - t0)
            
