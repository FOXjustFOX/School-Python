liczba= int(input())

plan = [int(x) for x in input().split(" ")] # zbiera, rozdziela i zamienia liczby na int (w jednej linii)
#zamień sobie na input().split(" ") oraz poprzez pętlę for zamień na int

for i in range(1, len(plan)-1): # dla każdego elementu listy
    if plan[i-1] == 1 and plan[i+1] == 1: # jeśli są "1", przed i po
        plan[i] = 1 # zamień "i" na 1

print(plan.count(1)) # policz ile jest "1" i wypisz
