import time

t0 = time.time()

s = 0

while s < 2*10**5.6:
    s+=1
    
t1 = time.time()

print(t1-t0)    