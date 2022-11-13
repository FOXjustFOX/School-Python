import time
import sys


t0 = time.time()

a, b = 2,100000000#map(int, input().split(" "))

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


    # for n in range(2, limit+1):
    #     if sieve[n]:
    #         suma = 0
    #         f = n
    #         while f > 0:
    #             suma += f%10
    #             f = f // 10

    #         suma2 = 0
    #         g = n
    #         while g > 0:
    #             suma2 += g%2
    #             g = g // 2

    #         if sieve[suma] == True and sieve[suma2] == True and n >= d:
    #             # print(n, end=" ")
    #             yes += 1

    t1 = time.time()
    # print("Ile liczb: ",yes)
    

    
    
    print("Time: ", t1-t0)



def Atkin_2(d, limit):

    # t0 = time.time()

    if d<2:     # checking if the range is correct
        d=2
    limit += 1

    # sieve Eratostnesa
    E = [True]*limit
    E[1] = False
    for i in range(2,int(limit**0.5+1)):
        if E[i] == True:
            for j in range(2*i,limit,i):
                E[j] = False

    # digit sum
    def ds(n,s):
        suma = 0
        while n>0:
            suma += n%s
            n //= s
        return suma
    
    suma = 0

    #algorythm
    for i in range(d,limit):
        if E[i]==True:
            if E[ds(i,10)] and E[ds(i,2)]:
                suma += 1

    # print(suma)

    t1 = time.time()

    print("time: ", t1 - t0)


def pioter_better(a,b):
    from time import time

    # a, b = 2, 10#[int(x) for x in input().split()] # a >= 2

    b += 1

    # t0 = time()

    sbp = 0


    pn = [True] * (b)
    pn[1] = False


    #eratostenes
    for i in range(2, int(b**0.5)):   
        if pn[i]:
            for j in range(2 * i, b, i):
                pn[j] = False


    def nt(n,s):
        """returns digit sum or bit sum

        Args:
            n (int): number to sum
            s (int): 10 or 2 relative to the calculation that we want to perform

        Returns:
            int: sum that we wanted
        """
        
        suma = 0
        while n > 0:
            suma += n%s
            n //= s
        return suma


    for i in range(a,b):
        if pn[i]:
            if pn[nt(i,2)] and pn[nt(i,10)]:
                sbp += 1
                # print(i)

    print(sbp)


def badass(a,b):
    x = 1
    with open("test.txt", "r") as file:
        lista = file.readline()
        
    while True:
        try:
            c = lista.index(str(a))
            d = lista.index(str(b))
            
        except ValueError:
            if x == 1:
                a += 1
                x = 2
            else:
                b -= 1
                x = 1
        else:
            print(len(lista[c:d]))
            break

#eratost(a, b)

#other(a, b)

atkin(a, b)


# just for printing into the file
# with open("test.txt", "w") as file:
#     sys.stdout = file
Atkin_2(a, b)

# badass(a,b)

#this is the best one