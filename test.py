# import time


# d, limit = map(int, input().split(" "))

# t0 = time.time()

# tab = []


# if limit > 2:
#     tab.append(2)
# if limit > 3:
#     tab.append(3)

# sieve = [False] * (limit + 1)
# for i in range(0, limit + 1):
#     sieve[i] = False


# x = 1
# while x * x <= limit:
#     y = 1
#     while y * y <= limit:

    
#         n = (4 * x * x) + (y * y)
#         if (n <= limit and (n % 12 == 1 or
#                             n % 12 == 5)):
#             sieve[n] ^= True

#         n = (3 * x * x) + (y * y)
#         if n <= limit and n % 12 == 7:
#             sieve[n] ^= True

#         n = (3 * x * x) - (y * y)
#         if (x > y and n <= limit and
#                 n % 12 == 11):
#             sieve[n] ^= True
#         y += 1
#     x += 1

# r = 5
# while r * r <= limit:
#     if sieve[r]:
#         for i in range(r * r, limit+1, r * r):
#             sieve[i] = False

#     r += 1

    
# for a in range(5, limit+1):
#     if sieve[a]:
#         tab.append(a)


# yes = []

# for n in tab:
#     if n >= d:
#         #if bin(n).count("1") in tab:
#         #if sum(int(char) for char in str(n)) in tab:# and bin(n).count("1") in tab:
#         yes.append(n)

# t1 = time.time()

# print(len(yes))

# print(t1-t0)

# n=int (input ("Enter a number: "))
# b= []
# while(n>0):
#     d=n%2
#     b.append(d)
#     n=n//2
# b.reverse()

# s = ""

# print("Binary Equivalent is: ")
# for i in b:
#     s += str(i)
# print(s, end="\n")