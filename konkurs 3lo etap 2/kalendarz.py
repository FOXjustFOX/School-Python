
arbuzan, bananit = map(int, input().split(" "))

arbuzandni = [0] * (arbuzan + 1)
bananitdni = [0] * (bananit + 1)

e = 1
for j in input().split(" "):
    arbuzandni[e] = int(j) + arbuzandni[e-1]
    e += 1

e = 1
for j in input().split(" "):
    bananitdni[e] = int(j) + bananitdni[e-1]
    e += 1

for i in range(int(input())):
    dzien, miesiac, kalendarz = input().split(" ")

    dzien = int(dzien)
    miesiac = int(miesiac)

    if kalendarz == "A":

        dni = dzien + arbuzandni[miesiac ]

        for h in range(bananit ):
            if dzien <= bananitdni[h]:
                g = (bananitdni[h ] - dzien)
                print(g if g > 0 else g*-1, h)
                break
    else:

        dni = dzien + bananitdni[miesiac ]

        for h in range(arbuzan ):
            if dzien <= arbuzandni[h]:
                v = (arbuzandni[h ] - dzien)
                print(v if v > 0 else v*-1, h)
                break






# 1 2
# 2 1
# 4 3
# 1 6