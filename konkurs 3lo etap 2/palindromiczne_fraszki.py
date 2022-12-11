#working TOO SLOW, 40% on szkopuł

from time import time

n = int(input())

words = [''] * n


def good(a):
    m = []
    znaki = [",", " ", ".", "-"]

    for i in znaki:
        if i in a:
            return ''.join([x for x in a if x not in znaki])

    return a


for i in range(n):
    words[i] = good(input())

t0 = time()

c = 0
i = 0
j = 0

for word in words:
    for other in words:
        if i != j:
            c_word = word + other
            if c_word == c_word[::-1]:
                c += 1
        j += 1
    j = 0
    i += 1

print(c)

print("normal ", "%.10f" % (time() - t0))
