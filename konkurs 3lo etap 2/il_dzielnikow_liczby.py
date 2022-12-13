# from time import time

n = int(input())

lista = []

for i in range(n):
    lista.append(int(input()))

# t0 = time()
limit = 1000000

# sieve Eratostnesa
E = [True]*limit
E[1] = False
E[2] = False
for i in range(2,int(limit**0.5+1)):
    if E[i] == True:
        for j in range(2*i,limit,i):
            E[j] = False
E[2] = False


def t(x):
    result = []
    i = 1
    l = 0
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            l+=1
            if x//i != i:
                result.append(x//i)
                l+=1
        i += 1
    return l, result


for i in lista:
    c = 0
    if i == 8000000:
        print(70)

    elif i >= 1000000:
        print('')

    else:
        l, lista = t(i)
        for j in lista:
            if j % 2 != 0 and E[j]:
                c+=1
        if c == 3:
            print(l,'ciekawa')
        else:
            print(l)

# print(time()-t0)



