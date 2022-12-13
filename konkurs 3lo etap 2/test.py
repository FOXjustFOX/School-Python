def break_palin(s):
    i = 1
    j = 0
    mylist = []
    while i < len(s):
        if s[i] == s[j]:
            mylist.append(s[j:i+1])
            j = i + 1
            i = i + 2
        else:
            i += 1
    return ' '.join(mylist)

print(break_palin('abccba'))

print(break_palin('abcba'))
