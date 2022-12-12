#working TOO SLOW, 40% on szkopuł

from time import time
import itertools


def good(a):
    m = []
    znaki = [",", " ", ".", "-"]

    return a.translate({ord(i): None for i in znaki})


n = int(input())

words = [''] * n

for i in range(n):
    words[i] = good(input())

t0 = time()

c = 0
i = 0
j = 0


for word in words:
    for other in words:
        # if i != j:
        c_word = f'{word}{other}'
        # c_word = ''.join([word, other])
        # c_word = word + other
        if c_word == c_word[::-1]:
            c += 1
        # j += 1
    # j = 0
    # i += 1

print(c)

print("normal ", "%.10f" % (time() - t0))
