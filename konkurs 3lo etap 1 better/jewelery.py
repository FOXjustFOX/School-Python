l = int(input())

w = []

for i in range(l):
    word = input()
    w.append(word)

w.sort(key=len)

def divideList(lst):
    dct = {}
 
    for element in lst:
        if len(element) not in dct:
            dct[len(element)] = [element]
        elif len(element) in dct:
            dct[len(element)] += [element]
     
    res = []
    for key in sorted(dct):
        res.append(dct[key])
     
    return res

w = divideList(w)

for i in w:
    i.sort()
    for j in i:
        print(j)