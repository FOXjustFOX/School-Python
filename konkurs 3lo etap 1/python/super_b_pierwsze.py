
def SBP(d, limit):


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


    suma = []

    #algorythm
    for i in range(d,limit):
        if pn(i)==True:
            if pn(ds(i,10)) and pn(ds(i,2)):
                suma.append(i)
    print(len(suma))



a,b = map(int, input().split())

SBP(a,b)