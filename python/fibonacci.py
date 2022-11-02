a = 1
b = 1

n = int(input("Podaj liczbę znaków: "))

for _ in range(10):
    print(a, end=" ")
    a,b = b, a+b

print(end="\n")

