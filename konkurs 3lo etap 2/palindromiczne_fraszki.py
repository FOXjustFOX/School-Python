from time import time
from itertools import permutations

znaki = [",", " ", ".", "-"]

def good(a):
    m = []

    return a.translate({ord(i): None for i in znaki})


with open('konkurs 3lo etap 2/test.txt', 'r') as f:
    n = int(f.readline())

    words = [''] * n

    for i in range(n):
        words[i] = good(f.readline().strip())

# t0 = time()

c = 0
    
for i in permutations(words, 2):
    c_word = f'{i[0]}{i[1]}'
    g_word = f'{i[1]}{i[0]}'
    if c_word == c_word[::-1]:
        c += 1
    if g_word == g_word[::-1]:
        c += 1

print(int(c/2))

print("time: ", "%.10f" % (time() - t0))


