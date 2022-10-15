import time


a, b = map(int, input().split(" "))

t0 = time.time()

if a<2:     # checking if the range is correct
    a=2
b += 1

# sieve Eratostenesa
E = [True]*b                     
for i in range(2,int(b**0.5+1)):
    if E[i] == True:
        for j in range(2*i,b,i):
            E[j] = False

# digit sum
def ds(n,s): 
    suma = 0
    while n>0:
        suma += n%s
        n //= s
    return suma

# if prime number
def pn(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True


suma = 0

#algorythm
for i in range(a, b):
    if E[i]==True:
        if pn(ds(i,10))==True and pn(ds(i,2))==True:
            suma += 1

print(suma)

t1 = time.time()

print("time: ", t1 - t0)