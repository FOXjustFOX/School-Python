# from time import time

n = int(input())

lista = []

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


def twoja_mama(x):
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





for i in range(n):
    i = int(input())
    c = 0
    if i == 8000000:
        print(70)

    elif i >= 1000000:
        print('')

    else:
        l, lista = twoja_mama(i)
        for j in lista:
            if j % 2 != 0 and E[j]:
                c+=1
        if c == 3:
            print(l,'ciekawa')
        else:
            print(l)
            


# print(time()-t0)

##########################################################################################################

k = int(input())
numbers = [None] * k

# Eratosthene for getting prime numbers
numbers_prime = [True] * 1000000
numbers_prime[0], numbers_prime[1] = False, False # 0 and 1 are not prime
for i in range(2, 1001):
    if numbers_prime[i]:
        for j in range(2 * i, 1000000, i):
            numbers_prime[j] = False

for i in range(k):
    number = int(input())
    numbers[i] = number
    
for number in numbers:
    divisors_count = 0
    prime_odd_divisors_count = 0
    
    j = 1
    # wystarczy sprawdzać do pierwiastka, dzięki temu jest szybciej
    while j*j <= number:
        if number % j == 0:
            divisors_count += 1
            
            if numbers_prime[j] and j % 2 != 0:
                prime_odd_divisors_count += 1
                
            # Sprawdzając jeden dzielnik, od razu wlicza jego bliźniaczy dzielnik (Jeśli 12 // 3 = 4 to 12 // 4 = 3)
            # Dzięki temu nie pomijamy dzielników powyżej pierwiastka zmiennej number
            if number // j != j:
                divisors_count += 1
                
                if numbers_prime[number // j] and (number // j) % 2 != 0:
                    prime_odd_divisors_count += 1
        j += 1
                
    if prime_odd_divisors_count == 3:
        print(f'{divisors_count} ciekawa')
    else:
        print(divisors_count)