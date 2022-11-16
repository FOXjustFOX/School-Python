n, k = map(int, input().split(" "))

w = {}
p = []

# adding the castles to the graph dictionary
for i in range(1, n):
    a, b, c = map(int, input().split(" "))

    if a not in w:
        w[a] = {b: c}
    else:
        w[a][b] = c

    if b not in w:
        w[b] = {a: c}
    else:
        w[b][a] = c

# adding the knights to the list
for i in range(n, n + k):
    p.append(int(input()))

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


podr = []

for i in range(k):
    dist = 0
    # each day one nwe castle is built
    g = Graph(w)
    podr.append(p[i])
    main = p[i]
    sec = []
    king = False

    if len(podr) == 1:
        g.dfs(1, p[i])
        dist += g.get_dist() * 2  # *2 because the knight has to go back to the castle
    else:
        for j in range(len(podr) - 1):
            g.dfs(podr[j], podr[j + 1])
            dist += g.get_dist() * (len(podr) + 1)

        g.dfs(podr[-1], 1)
        dist += g.get_dist()

    print(dist)



