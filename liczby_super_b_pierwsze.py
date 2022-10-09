import time

t0 = time.time()

a, b = map(int, input().split(" "))

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
        if bin(n).count("1") in tablica and sum(int(char) for char in str(n)) in tablica and n >= a:
            yes.append(n)


    print(yes)

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

    print(tab2)
    t1 = time.time()

    print("time other: ", t1-t0, end="\n")










def SieveOfAtkin(d, limit):
    
    t0 = time.time()
    
    tab = []

    # 2 and 3 are known
    # to be prime
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")
 
    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False
 
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
 
            # Main part of
            # Sieve of Atkin
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
 
    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
 
        r += 1
 
        # Print primes
    # using sieve[]
    for a in range(5, limit+1):
        if sieve[a]:
            #print(a, end=" ")
            tab.append(a)
    
    
    yes = []

    for n in tab:
        if bin(n).count("1") in tab and sum(int(char) for char in str(n)) in tab and n >= d:
            yes.append(n)

    print(len(yes))

    t1 = time.time()

    print("atkin: ", t1 - t0)



eratost(a, b)

other(a, b)

SieveOfAtkin(a, b)