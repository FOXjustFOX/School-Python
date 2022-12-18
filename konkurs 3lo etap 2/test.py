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

        dni = dzien + arbuzandni[miesiac - 1]

        for h in range(bananit + 1):
            if dni <= bananitdni[h]:
                print(abs(bananitdni[h - 1] - dni), h)
                break
    else:

        dni = dzien + bananitdni[miesiac - 1]

        for h in range(1, arbuzan + 1):
            if dni <= arbuzandni[h]:
                print(dni - arbuzandni[h - 1], h)
                break