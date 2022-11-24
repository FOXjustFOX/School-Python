n = int(input())

num = [False,True] * 1000000

def calculate_prime_factors(N):
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
    while N % 2 == 0:
        N = N // 2
        if N == 1:
            return prime_factors
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.add(factor)
            while N % factor == 0:
                N = N // factor
                if N == 1:
                    return prime_factors
                
def check_calculation(N):
    
    for i in N:
        if num[i] == False:
            return False
    return True


for i in range(n):
    number = int(input())
    prime_factors = calculate_prime_factors(number)
    prime = False
    
    nod = 0
    
    if number > 0:
        for j in range(1, int(number/2) + 1): 
            if number % j == 0:       
                nod += 1
        nod += 1
    
    
    print(nod) if not check_calculation(prime_factors) else print(f"{nod} ciekawa")
    
    # for i in range(len(prime_factors)):
    #     if prime_factors[i]:
    #         print(i, end=" ")
