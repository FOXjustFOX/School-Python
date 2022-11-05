n = int(input())
jewels = []

for i in range(n):
    jewels.append(input())

jewels.sort(key= lambda x: (len(x) + 1) ** 15 + ord(x[0]))

for i in range(len(jewels)):
    try:
        jewel = jewels[i]
        nexjewel = jewels[i+1]
    except IndexError:
        pass
    else:
        if len(jewel) == len(nexjewel):
            j = 0
            while jewel[j] == nexjewel[j]:
                j+=1

            else:
                if ord(jewel[j]) > ord(nexjewel[j]):
                    jewels[i], jewels[i+1] = nexjewel, jewel


for jewel in jewels:
    print(jewel)