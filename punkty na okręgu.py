r = int(input())

on = 0
ins = 0

for x in range(1,r+1):
    for y in range(0,r+1):
        if (x**2+y**2)**0.5 == r:
            # print(x,y, end=", ")
            on += 1
        elif (x**2+y**2)**0.5 < r:
            ins += 1

print(on*4, ins*4+1)#+1 because of (0,0) point



