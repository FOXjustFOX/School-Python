def my_jewelery():

    liczba = int(input())
    bizuteria = []
    for i in range(liczba):
        word = input()
        bizuteria.append(word)
    bizuteria.sort(key=len)
    def rozdziel_liste(lst):
        slownik = {}
        for element in lst:
            if len(element) not in slownik:
                slownik[len(element)] = [element]
            elif len(element) in slownik:
                slownik[len(element)] += [element]
        rozdzielona_lista = []
        for key in slownik:
            rozdzielona_lista.append(slownik[key])
        return rozdzielona_lista
    bizuteria = rozdziel_liste(bizuteria)
    for i in bizuteria:
        i.sort()
        for j in i:
            print(j)

def wiktor_jewelery():

    ilosc = int(input())
    bizuteria = []
    for i in range(ilosc):
        dana = input()
        bizuteria.append(dana)
    bizuteria.sort()
    bizuteria.sort(key=len)
    for z in bizuteria:
        print(z)
