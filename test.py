def t(x):
    l = 0
    for i in range(1,x+1):
        if x % i == 0:
            l+=1
    return l


with open("test.txt", "w") as file:
    for i in range(1000000):
        if i == 0:
            file.write(f'if i == {i}:\n    print({t(i)})\n')
        else:
            file.write(f'elif i == {i}:\n    print({t(i)})\n')

