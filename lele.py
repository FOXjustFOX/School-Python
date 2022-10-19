
l = int(input())

w = []#['abba', 'bbaa', 'aabb', 'baab', 'abab', 'baba', 'tsttt', 'ttttt', 'stsss', 'stttt']

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


def char_frequency(word):
    frequency  = {}
    for char in word:
        #if character  is in frequency then increment the value
        if char in frequency:
            frequency[char] += 1
        #else add character and set it to 1
        else:
            frequency[char] = 1
    return frequency 


w = divideList(w)
yes = {

}

s = 1

for i in w:
    if len(i) > 1:
        for j in i:
            s = 0
            while True:
                if len(j)+s in yes:
                    if yes[len(j)+s][0] == j:
                        break
                    if char_frequency((yes[len(j) + s])[0]) == char_frequency(j):
                        yes[len(j)+s].append(j)
                        break
                        
                    else:
                        s+=1
                        
                else:
                    yes[len(j)+s] = [j]
                    break
                    

    else:
        yes[len(i[0])] = [i[0]]

w = []

for v in yes.values():
    v.sort()
    w.append(v)

w.sort()

for i in w:
    print(' '.join(i))
