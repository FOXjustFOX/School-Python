a = str(input("podaj ciąg: "))
x = 0
y = 0

l = a.split(" ")
print(l)

for i in l:
    if i[1] == "G":
        y+= int(i[0])
    elif i[1] == "D":
        y -= int(i[0])
    elif i[1] == "L":
        x -= int(i[0])
    elif i[1] == "R":
        x += int(i[0])

print(x, y)