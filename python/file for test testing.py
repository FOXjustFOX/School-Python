d, limit = map(int, input().split(" "))

tab = []

yes = 0


sieve = [False] * (limit + 1) #to je to samo?

if limit > 2:
    sieve[2] = True
    
if limit > 3:
    sieve[3] = True


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

        if sieve[suma] and sieve[suma2] and n >= d:
            yes += 1
        


print(yes)

