a,b = input().split(" ")
a = int(a)
b = int(b)


def nwd(a, b): return nwd(b, a%b) if b else a


print(a*b//nwd(a,b))
