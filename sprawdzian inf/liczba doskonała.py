a = int(input("podaj liczbę: ")) #wprować zmienną której dzielników będziemy szukać
wyniki = [] # tworzymy listę, w którą włożymy dzielniki liczby a
suma = 0

while True:
    if a > 0:   #sprawdza czy liczba jest liczbą naturalną
        for i in range(1, int(a/2) + 1): #iterujemy od jedynki, do połowy liczby x - dzielenie przez wiecej niż połowe nie da całkowitego wyniku
            if a % i == 0:       #jeżeli liczba i  jest dzielnikiem liczby x
                wyniki.append(i) #to dodaj ją do listy wyników 

        for i in wyniki:
            suma += i
            
        if suma == a:
            print("Tak! liczba", a, "jest liczbą doskonałą")
            break

        else:
            print("nie!!!")
            break

    else:
        print("Błąd, niewłaściwe dane")
        break