import itertools

mylist = ["hello", "world", "world", "bar"]

for a, b in itertools.combinations(mylist, 2):
    print(a, b)