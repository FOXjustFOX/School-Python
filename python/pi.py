s = 1

for n in range(1,int(input())):
    s *= ((2*n)/(2*n-1))*((2*n)/(2*n+1))
    # if n % 2 == 0:
    # s += (-1**n)/(2*n+1)
    
print(s*2)