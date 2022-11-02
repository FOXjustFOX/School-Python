# program ma za zadanie sprawidzić czy i jakie obrazy zostały skradzione

a = int(input()) # liczba obrawów w galerii

#obrazy = [int(x) for x in input().split(" ")]
#   to samo co na dole, ale w jednej linii

obrazy = input().split(" ") # podziel string wejściowy na listę stringów

for i in range(len(obrazy)): # dla każdego elementu listy
  obrazy[i] = int(obrazy[i])    # zamień string na int


lost = [] # lista z indeksami obrazów, które zostały skradzione


obrazy = sorted(obrazy) # posortuj listę obrazów

for i in range(obrazy[0], obrazy[-1]+1): # dla każdego obrazu od pierwszego do ostatniego
    if i not in obrazy: # jeśli obrazu nie ma na liście
        lost.append(i) # dodaj go do listy skradzionych
        

if len(lost) == 0: # jeśli lista jest pusta
    print(0) # wypisz 0
else: # jeśli nie jest pusta
    print(len(lost)) # wypisz długość listy
