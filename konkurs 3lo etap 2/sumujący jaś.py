n = int(input())
suma = 0
l = 1
# this is the function that sums the numbers

for i in range(n):
    x = (input()).replace(",", ".")
    x = float(x)
    suma += x

for i in range(len(str(suma))):
    if suma - int(suma) != 0:
        if str(suma)[i] == str(suma)[i+1]:
            l = i
            break
    else:
        l = 0
        # print(int(suma))

if l == 0:
    print(int(suma))
else:
    print(str(round(suma,l)).replace(".", ","))

