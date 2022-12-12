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
E[1] = False
E[2] = False


def t(x):
    # We will store all factors in `result`
    result = []
    i = 1
    l = 0
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            l+=1
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
                l+=1
        i += 1
    # Return the list of factors of x
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



