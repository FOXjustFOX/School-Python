def Anagrams(lista):
    r = {}
    for word in lista:
        sW = ''.join(sorted(word))
        if sW not in r:
            r[sW] = [word]
        else:
            if word not in r[sW]:
                r[sW] += [word]
    for i in r:
        r[i] = sorted(r[i])
    for i in sorted(r.values()):
        print(*i)


l = int(input())
li = []
for i in range(l):
    w = input()
    li.append(w)
Anagrams(li)
