n = int(input())


limit = 1000000

E = [True]*limit
E[1] = False
for i in range(2,int(limit**0.5+1)):
    if E[i] == True:
        for j in range(2*i,limit,i):
            E[j] = False




for d in range(n):
    a = int(input())
    dzielniki = 0
    if a > 0:
        for i in range(1, int(a/2) + 1):
            if a % i == 0:
                dzielniki += 1

