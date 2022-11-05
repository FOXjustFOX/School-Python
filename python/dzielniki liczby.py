"""dzielniki liczb"""

a = int(input("podaj liczbę do wyznaczania dzialników: ")) #wprować zmienną której dzielników będziemy szukać
wyniki = [] # tworzymy listę, w którą włożymy dzielniki liczby a



if a > 0:   #sprawdza czy liczba jest liczbą naturalną 
    for i in range(1, int(a/2) + 1): # iterujemy od jedynki, do połowy liczby x - dzielenie przez wiecej niż połowe nie da całkowitego wyniku
        if a % i == 0:       #jeżeli liczba i  jest dzielnikiem liczby x
            wyniki.append(i) #to dodaj ją do listy wyników 
    wyniki.append(a) #na koniec wypisujemy liczbe x - ona też jest swoim dzielnikiem
    print("Dzielników liczby", a, "jest", len(wyniki), "i są to:\n",wyniki, ) #tu można drukować sam wynik, ale tak jak jest, jest fancy
else:
    print("Błąd, niewłaściwe dane") #jeśli liczba nie jest naturalna wydrukuj to

