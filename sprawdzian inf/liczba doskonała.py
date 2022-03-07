a = int(input("podaj liczbę: ")) #wprować zmienną której dzielników będziemy szukać
wyniki = [] # tworzymy listę, w którą włożymy dzielniki liczby a
suma = 0

while True:
    if a > 0:   #sprawdza czy liczba jest liczbą naturalną
        for i in range(1, int(a/2) + 1): #iterujemy od jedynki, do połowy liczby x - dzielenie przez wiecej niż połowe nie da całkowitego wyniku
            if a % i == 0:       #jeżeli liczba i  jest dzielnikiem liczby x
                wyniki.append(i) #to dodaj ją do listy wyników 

        for i in wyniki: # dodajemy wszystkie dzielniki tej liczby
            suma += i
            
        if suma == a: # i sprawdzamy czy ta liczba jest równa sumie swoich dzielników
            print("Tak! liczba", a, "jest liczbą doskonałą")
            break

        else:
            print("nie!!!")
            break

    else:
        print("Błąd, niewłaściwe dane")
        break