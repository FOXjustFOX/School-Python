import time

a,b = map(int, input().split(" "))

c = [True]*a#['(', '(', ')', '(', '(', ')', ')', ')']

d = input()#['(', '(', '(', ')', ')', ')', '(', ')']#['(']*500000+[')']*500000#input()#

t0 = time.time()

inde = 0 # counts bracket pairs
mx = 0 # max vlaue of bracket pair
p = 0 # place of the greatest bracket pair
changes = 0 # value of changes made to the list
ph = 0


for i in d:
    if i == ")":
        c[ph] = False
    ph += 1
    c.append(i)

# print(c)

for z in range(int(len(c)/2)):

    # print("here")

    for i in range(len(c)):
        if c[i] == '(':
            # print(i)
            inde += 1

            if inde > mx:
                mx = inde
                p = i - 1

        elif inde != 0 and c[i] == ')':
            # print("minus")
            inde -= 1
            
    # print("\n", mx, p)

    if mx <= b:
        print(c)
        print(changes)
        break
    
    # print("\n",mx, p, changes)

    c[p] = ')' if c[p] == '(' else '('
    c[p+1] = '(' if c[p] == ')' else ')'
    changes += 2
    # print(c)
    
    mx = 0
    
# 
# print("\n",mx, p, changes)

t1 = time.time()

print(t1-t0)