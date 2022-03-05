from math import *
a = int(input("Podaj liczbę do której będziemy wyznaczać: "))
tablica = [True] * (a+1)  #tworzymy tablicę z wartościami True o długości 'a+1'


for i in range(2, int(sqrt(a))):    #iterujemy poprzez nią, zaczynajac od 2, a konczać na zaokrąglonym pierwiastku z 'a'
    if tablica[i]:  #jeśli 'i' w tablicy ma wartość True to ...
        for j in range(i*i, a+1, i): #zamieniamy wszystkie wielokrotności 'i' w tablicy na False
            tablica[j] = False
        
for b in range(2, a+1): #iterując przez tablicę sprawdzamy które 'i' mają wartość true i drukujemy ich miejsce w tablicy
    if tablica[b]:
        print(b, end=' ')

            