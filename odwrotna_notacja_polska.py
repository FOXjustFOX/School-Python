signs = ["+", "-", "/", "*", "**"]  #lista znaków
stos = []   #pusta lista na której będziemy pracować


eq = input().split(" ") #bierze informacje od urzytk. i rozdziela je, po spacjach i pakuje w listę


for i in eq:    #zmienna i będzie przyjmowała każdą wartość z listy eq

    if i in signs:  #jeśli i jest w liście znaków

        b = stos.pop() #    usuwamy ostatnią liczbę ze stosu i zapisujemy ją pod b
        a = stos.pop() #    to samo dla a

        if i == "+": #  liczymy a,b zależnie od znaku
           c = a+b

        if i == "-":
           c = a-b

        if i == "*":
           c = a*b

        if i == "/":
           c = a/b

        if i == "**":
           c = a**b

        stos.append(c) #    a potem zapisujemy wynik liczenia na końcu stosu


    else: #     jeśli i jest liczbą

        i = float(i) #  to zamieniamy jej typ na zmiennoprzecinkowy

        stos.append(i) #    i dodajemy do stosu


print(stos[0]) #    na końcu drukujemy pierwszy (i jedyny) element stosu (wynik)