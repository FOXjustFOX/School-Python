liczba = int(input())

schody = [int(x) for x in input().split(" ")] # zbiera, rozdziela i zamienia liczby na int (w jednej linii)
#zamień sobie na input().split(" ") oraz poprzez pętlę for zamień na int

print(schody.count(1)) # policz ile jest pierwszych schoków i wypisz

for i in range(1,len(schody)): # dla każdego elementu listy
    if schody[i] == 1: # jeśli jest "1"
        print(schody[i-1], end=" ") # wypisz poprzedni schodek
print(schody[-1]) # wypisz ostatni schodek