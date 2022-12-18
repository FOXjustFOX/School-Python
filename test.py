k = int(input())
numbers = [None] * k

# Eratosthene for getting prime numbers
numbers_prime = [True] * 1000000
numbers_prime[0], numbers_prime[1] = False, False  # 0 and 1 are not prime
for i in range(2, 1001):
    if numbers_prime[i]:
        for j in range(2 * i, 1000000, i):
            numbers_prime[j] = False

for i in range(k):
    number = int(input())
    numbers[i] = number


def t(x):
    result = []
    i = 1
    l = 0
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            l+=1
        i += 1
    return l, result


for number in numbers:
    divisors_count, l = t(i)
    prime_odd_divisors_count = 0

    for divisor in l:
        if divisor % 2 != 0 and numbers_prime[divisor]:
            prime_odd_divisors_count += 1

    if prime_odd_divisors_count == 3:
        print(f'{divisors_count} ciekawa')
    else:
        print(divisors_count)