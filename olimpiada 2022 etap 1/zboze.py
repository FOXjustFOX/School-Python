with open("input.txt", "r") as f:
    x = f.readlines()

n, k = map(int, x[0].split(" "))

w = {}
p = []


# adding the castles to the graph dictionary
for i in range(1, n):
    a, b, c = map(int, x[i].split(" "))

    if a not in w:
        w[a] = {b: c}
    else:
        w[a][b] = c

    if b not in w:
        w[b] = {a: c}
    else:
        w[b][a] = c

# adding the knights to the list
for i in range(n, n+k):
    p.append(int(x[i]))


print(w)
print(p)


# graph class

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.path = []
        self.dist = 0

    def dfs(self, start, end):
        self.visited.add(start)
        self.path.append(start)
        if start == end:
            return self.path
        for neighbour in self.graph[start]:
            if neighbour not in self.visited:
                self.dist += self.graph[start][neighbour]
                self.dfs(neighbour, end)
                if end in self.path:
                    return self.path
                else:
                    self.path.pop()
                    self.dist -= self.graph[start][neighbour]

    def get_dist(self):
        return self.dist

    def get_path(self):
        return self.path


for i in range(k):
    dist = 0
    # each day one nwe castle is built
    g = Graph(w)

    if i == 0: # if it's the first day
        g.dfs(p[i], 1) # find the path from the king to the castle
        dist += g.get_dist() # add the distance to the total distance
    else: # if it's not the first day
        for j in range(i): # for each castle
            if p[i] != p[j]: # if the castle is not the same as the previous one
                g.dfs(p[i], p[j]) # find the shortest path between the two castles
                dist += g.get_dist()*2 # add the distance to the total distance

    print(dist*2)

# {1: {4: 3, 3: 6, 2: 5}, 4: {1: 3, 5: 1}, 3: {1: 6}, 2: {1: 5}, 5: {4: 1}}


# print(Graph(w).get_dist())


