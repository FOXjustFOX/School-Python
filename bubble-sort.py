import random
import time

L = []
n = 200

for i in range(n):
    L.append(int(random.randint(0, 1000)))

t = time.time()

for j in range(n-1):
    for i in range(n-1-j):
        if L[i]> L[i+1]:
            L[i], L[i+1] = L[i+1] , L[i]

time = time.time() - t

print("czas sortowania", time)
