from time import time

znaki = [",", " ", ".", "-"]

def good(a):
    m = []

    return a.translate({ord(i): None for i in znaki})


with open('test.txt', 'r') as f:
    n = int(f.readline())

    words = [''] * n

    for i in range(n):
        words[i] = good(f.readline().strip())




t0 = time()

c = 0
i = 0
j = 0


for word in words:
    for other in words:
        if i != j:
            c_word = f'{word}{other}'
            if c_word == c_word[::-1]:
                c += 1
        j += 1
    j = 0
    i += 1

print(c)

print("time: ", "%.10f" % (time() - t0))
