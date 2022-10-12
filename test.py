import time


d, limit = map(int, input().split(" "))
t0 = time.time()

tab = []

yes = 0


sieve = [False] * (limit + 1) #to je to samo?
# for i in range(0, limit + 1):
#     sieve[i] = False
# bin(2) nie jest liczbą pierwszą
if limit > 2:
    sieve[2] = True
    
if limit > 3:
    sieve[3] = True
    # yes += 1 #3 jest

'''Mark sieve[n] is True if
one of the following is True:
a) n = (4*x*x)+(y*y) has odd
number of solutions, i.e.,
there exist odd number of
distinct pairs (x, y) that
satisfy the equation and
n % 12 = 1 or n % 12 = 5.
b) n = (3*x*x)+(y*y) has
odd number of solutions
and n % 12 = 7
c) n = (3*x*x)-(y*y) has
odd number of solutions,
x > y and n % 12 = 11 '''

x = 1
while x * x <= limit:
    y = 1
    while y * y <= limit:

    
        n = (4 * x * x) + (y * y)
        if (n <= limit and (n % 12 == 1 or
                            n % 12 == 5)):
            sieve[n] ^= True

        n = (3 * x * x) + (y * y)
        if n <= limit and n % 12 == 7:
            sieve[n] ^= True

        n = (3 * x * x) - (y * y)
        if (x > y and n <= limit and
                n % 12 == 11):
            sieve[n] ^= True
        y += 1
    x += 1

r = 5
while r * r <= limit:
    if sieve[r]:
        for i in range(r * r, limit+1, r * r):
            sieve[i] = False

    r += 1


for n in range(2, limit+1):
    if sieve[n]:
        suma = 0
        f = n
        while f > 0:
            suma += f%10
            f = f // 10

        suma2 = 0
        g = n
        while g > 0:
            suma2 += g%2
            g = g // 2

        if sieve[suma] == True and sieve[suma2] == True and n >= d:
            yes += 1
        


print(f"\nLiczba super-b-pierwszych w zakresie {d} do {limit:,}:\n".replace(",", "."),yes, "\n")

t1 = time.time()

print("working time: %.5fs" %(t1-t0))


#good 10570
#bad 10547
# where 23??????????