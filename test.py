V, E = map(int, input().split())

adj = [] # lista list
for j in range(V+1):
    adj.append([])

for i in range(E):
    a, b = map(int, input().split())
    adj[a].append(b) # lista sąsiadów wierzchołka "a"
    adj[b].append(a) # lista sąsiadów wierzchołka "b"

print(adj)
visited = [False]*(V+1)
parent = [0]*(V+1)

# kolejka
visited[1] = True
Q = [1]
while len(Q)>0:
    x = Q[0]
    Q.pop(0) # usuwa początkowy element z kolejki
    for y in adj[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            Q.append(y)
print(parent, "\n")

for i in range(len(parent)):
    print(parent[i],": ", adj[i])