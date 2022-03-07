def dzielniki(liczba):

    wyniki = [] 

    if liczba > 0:   #sprawdza czy liczba jest liczbą naturalną
        for i in range(1, int(liczba/2) + 1): #iterujemy od jedynki, do połowy liczby x - dzielenie przez wiecej niż połowe nie da całkowitego wyniku
            if liczba % i == 0:       #jeżeli liczba i  jest dzielnikiem liczby x
                wyniki.append(i) #to dodaj ją do listy wyników 
        return wyniki


def suma_dzielników(lista): #dodaje wszystkie dzielniki liczby z danej listy

    suma = 0
    for każdy in lista:
        suma += każdy

    return suma


def zaprzy(a, b): # sprawdza czy liczby są zaprzyjaźnione
    suma_dzielników_a = suma_dzielników(dzielniki(a)) # sumuje dzielniki liczby 'a'
    suma_dzielników_b = suma_dzielników(dzielniki(b)) # sumuje dzielniki liczby 'b'

    if suma_dzielników_a == b and suma_dzielników_b == a: # i je porównuje
        print("tak", a, "i", b, " to liczby zaprzyjaźnione!!")
    else:
        print("nie!!!")

a = int(input("podaj 1 liczbę: ")) # podajemy liczby któe chcemy sprawdzać
b = int(input("podaj 2 liczbę: "))

print(zaprzy(a, b)) # i wywołujemy funkcję z tymi liczbami