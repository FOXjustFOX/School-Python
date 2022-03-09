a = int(input("podaj 1 liczbę: "))
b = int(input("podaj 2 liczbę: "))

while a != b: #dopóki a nie jest równe b to iterujemy
    if a < b:   #jeśli a jest większe od b to zamień je miejscami
        a, b = b, a 
    a -= b #pod a wstawiamy liczbę a - b

print(int(a))


