"""szyfr ceara"""

# 1. Kod ASCII
ord("a")  # zamienia znak na liczbę w kodzie ASCII
ord("z")
chr(80)   # zamienia liczbę na odpowiedni znak (literę)

'''
# 2. Wypisz wszystkie litery alfabetu
for i in range(97,123):
    print(chr(i), end=" ")
print()     # poniżej duże litery
for i in range(65,91):
    print(chr(i), end=" ")

'''


# 3. Szyfr Cezara

# do sprawdzianu chyba będzie tylko potrzebne szyfrowanie 

#czyli tylko to:
def szyfr(t, k):
    k = k % 26
    print(t)
    for i in range(len(t)):         # len(t) - liczba znaków
        szyfr = ord(t[i])+k         # zamiana tekstu na liczby i dodanie klucza
        if szyfr>122:               # jeżeli przekroczymy zakres literek
            szyfr = szyfr - 26      # to wracamy na początek do litery a
        print(chr(szyfr), end="")   # zamiana zaszyfrowanej liczby na tekst



#to jest deszyfrowanie
def de_szyfr(t, k):
    k %= 26
    print(t)
    for i in range(len(t)):
        szyfr = ord(t[i])-k
        if szyfr < 96:
            szyfr += 26
        print(chr(szyfr), end='')

        

# a to kod który podaje czy użytkownik chce szyfrować czy deszyfrować
print("1 = szyfr")
print("2 = deszyfr")
a = int(input("szyfr czy deszyfr? "))
if a == 1:
    t = str(input("Podaj słowo do zaszyfrowania: ")) #podaj słowo do szyfrowania i zamień je na string
    k = int(input("Podaj klucz szyfrowania (liczba od 1 do 25): "))
    szyfr(t, k)

elif a == 2:
    t = str(input("Podaj słowo do odszyfrowania: ")) #podaj słowo do szyfrowania i zamień je na string
    k = int(input("Podaj klucz szyfrowania (liczba od 1 do 25): "))
    de_szyfr(t, k)
