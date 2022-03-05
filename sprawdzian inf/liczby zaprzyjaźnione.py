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


def zaprzy(a, b):
    suma_dzielników_a = suma_dzielników(dzielniki(a))
    suma_dzielników_b = suma_dzielników(dzielniki(b))

    if suma_dzielników_a == b and suma_dzielników_b == a:
        print("tak", a, "i", b, " to liczby zaprzyjaźnione!!")
    else:
        print("nie!!!")

b = int(input("podaj 1 liczbę: "))
c = int(input("podaj 2 liczbę: "))

print(zaprzy(b, c))