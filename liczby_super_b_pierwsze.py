import time

t0 = time.time()

a, b = 2,100#map(int, input().split(" "))

tablica = []



def eratost(a, b):

    tablica = []

    t0 = time.time()

    for c in range(2,b+1):
        tablica.append(c)

    t1 = time.time()

    for i in range(2, int(b**(1/2))):    #iterujemy przez tablicę 
        if i in tablica:    #jeśli 'i' znajduje się w tablicy to ...
            for j in range(i*i, b+1, i):    #dla wsystkich 'j'               w tablicy usuwamy wielokotności 'i'
                if j in tablica:                              #występujących
                    tablica.remove(j)

    yes = []

    for n in tablica:
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
        
        if suma in tablica and suma2 in tablica and n >= a:
            yes.append(n)


    print(*yes)

    t1 = time.time()

    print("time sito: ", t1-t0, end="\n")



def other(a, n):

    t0 = time.time()
    z = 0

    tab = []

    def prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i, w = 5, 2
        while i * i <= n:
            if n % i == 0:
                return False
            i, w = w + i, 6 - w
        return True
        
    def bin_sum(n):
        return bin(int(n)).count("1")

    def digit_sum(n):
        return sum(int(x) for x in str(n))

    for n in range(a, b+1):
        if prime(bin_sum(n)):
            tab.append(n) 

    tab2 = tab.copy()

    for i in range(len(tab)):
        i = tab[i]
        if not(prime(i) and prime(digit_sum(i))):
            tab2.remove(i)

    print(*tab2)
    t1 = time.time()

    print("time other: ", t1-t0, end="\n")



def atkin(d, limit):

    t0 = time.time()

    tab = []

    yes = 0

    sieve = [False] * (limit + 1) 

    if limit > 2:
        sieve[2] = True
        
    if limit > 3:
        sieve[3] = True


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
                print(n, end=" ")
                yes += 1

    t1 = time.time()
    print()#yes)    !!!!!!!!!! to powinno się drukowac
    
    print("time atkin: ", t1-t0)


    # print(f"\nLiczba super-b-pierwszych w zakresie {d} do {limit:,}:\n".replace(",", "."),yes, "\n")


    # print("working time: %.5fs" %(t1-t0))

eratost(a, b)

other(a, b)

atkin(a, b)