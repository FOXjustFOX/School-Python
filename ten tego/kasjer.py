# kasjer

liczby = [int(x) for x in input().split(" ")] # pobranie danych
n = liczby[0] # liczba klientów
w_time = liczby[1] # czas pracy kasjera
f_time = liczby[2] # czas pracy fajki

L = [0] * w_time # lista, która opisuje dzień pracy kasjera

for i in range(n): # dla każdego klienta
    m = [int(x) for x in input().split(" ")] # pobranie danych: czas przybycia, czas obsługi
    arrival = m[0] # czas przybycia
    time = m[1] # czas obsługi
    
    for j in range(arrival, arrival + time): # dla każdego momentu czasu, w którym klient jest w kasie
        L[j] = 1 # zajmie miejsce w kasie



lista = " ".join(map(str, L)) # zamień listę na string

#    tu jest spacja \/ żeby były odstępy między liczbami i na końcu jest ostatnie zero bez spacji 
print(lista.count(("0 "*(f_time - 1) +"0"))) # policz ile jest ("0" w ilości minut w przerwie) i wypisz