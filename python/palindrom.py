# taneczny palindrom
# wprowadzanie danych
liczby = [int(x) for x in input().split(" ")]# pobranie danych: l. tancerek, koszt strojów białych i czarnych
n = liczby[0] # liczba tancerek
b = liczby[1] # koszt strojów białych
c = liczby[2] # koszt strojów czarnych

L = [int(x) for x in input().split(" ")] # lista, która opisuje tancerki

for i in range(n): # dla każdej tancerki
    if L[i] == 1: # jeśli jest biała
        L[i] = b # zamień na koszt stroju białego
    elif L[i] == 2: # jeśli jest CZARNA
        L[i] = c # zamień na koszt stroju czarnego
        
cena = 0

for i in range(n): # dla każdej tancerki
    if L[i] == 0: # jeśli nie ma stroju
        L[i] = L[n - 1 - i]  # zamień na koszt stroju przeciwległej tancerki
        cena += L[i] # dodaj koszt stroju do ceny

if L == L[::-1]: # jeśli lista jest palindromem

    if n % 2 == 1: # jeśli jest nieparzysta liczba tancerzek (wtedy środkowa tancerka nie ma stroju)
        print(cena + min(b, c)) # wypisz sumę kosztów strojów + koszt stroju środkowej tancerki
    else: # jeśli jest parzysta liczba tancerzek
        print(cena) # wypisz sumę kosztów strojów
    
else:
    print("NIE") # jeśli lista nie jest palindromem, wypisz NIE
