"""zabwa tekstem"""

t = "1234567891011121314151617181920"

n = len(t)
licznik = 0

for i in range(n):
    if t[i] == "a":
        licznik += 1

#print(licznik)


print(
    t[0],"\n",
    t[1],"\n",
    t[3:6],"\n",
    t[7:],"\n",
    t[:7],"\n",
    t[ : :2],"\n",
    t[: :-1]
)



#print("tekst")
