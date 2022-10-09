from itertools import permutations 

l = 10#int(input())

w = ['liszka', 'tuba', 'tuba', 'klisza', 'kretes', 'anakonda', 'sekret', 'szalik', 'buta', 'tabu']

# for i in range(l):
#     word = input()
#     w.append(word)

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
        # for j in permutations(i,2):
        #     if char_frequency(j[0]) == char_frequency(j[1]):

        #         if (len(j[0]) in yes) and (j[0] in yes[len(j[0])]) and (j[1] in yes[len(j[0])]):
        #             break

        #         elif (len(j[0]) in yes) and (j[0] in yes[len(j[0])]):
        #             yes[len(j[0])] += j[1] + " "
                    
        #         elif len(j[0]) in yes and j[1] in yes[len(j[0])]:
        #             yes[len(j[0])] += j[0] + " "

        #         else:
        #             yes[len(j[0])] = j[0] + " "

        #     else:
        #         print("no", j[0], j[1])

        for j in i:
            if len(j) in yes:
                if yes[len(j)][0] != j:
                    if char_frequency((yes[len(j)])[0]) == char_frequency(j):
                        yes[len(j)].append(j)
                    
                    else:
                        yes[len(j)+s] = [j]
                
            elif len(j)+s in yes:
                if yes[len(j)+s][0] != j:
                    if char_frequency(yes[len(j)+s[0]]) == char_frequency(j):
                        yes[len(j)+s].append(j)
                    

            else:
                yes[len(j)] = [j]

    else:
        yes[len(i[0])] = [i[0]]

for v in yes.values():
    v.sort()

print(yes)