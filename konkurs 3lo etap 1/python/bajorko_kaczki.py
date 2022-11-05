a,b = input().split(" ")
a = int(a)
b = int(b)


def nwd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(a*b//nwd(a,b))
