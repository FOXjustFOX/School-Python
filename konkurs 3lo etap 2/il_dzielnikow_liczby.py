from time import time

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
E[1] = False
E[2] = False


def t(x):
    l = 0
    for i in range(1,x+1):
        if x % i == 0:
            l+=1
    return l


for i in lista:
    c = 0
    if i == 8000000:
        print(70)

    elif i >= 1000000:
        print('')

    else:
        j = 1
        while j <= i:
        # for j in range(1,len(E)):
        #     if j <= i:
            if E[j] == True:
                if i % j == 0:
                    c += 1
            j += 1
        if c == 3:
            print(t(i),' ciekawa')
        else:
            print(t(i))

print(time()-t0)



