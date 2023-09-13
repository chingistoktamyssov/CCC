from collections import deque

n, m = [int(x) for x in input().split()]

pho = [False for i in range(n)]
for i in [int(x) for x in input().split()]:
    pho[i] = True

toPrune = [0 for i in range(n)]
graph = [[] for i in range(n)]

for i in range(n-1):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

    toPrune[a] += 1
    toPrune[b] += 1

leaf = [False for i in range(n)]
queue = deque([])
for i in range(n):
    if toPrune[i] == 1:
        queue.append(i)
        leaf[i] = True
while queue:
    node = queue.popleft()
    if not  pho[node]:
        for i in graph[node]:
            toPrune[i] -= 1
            if toPrune[i] <= 1 and not leaf[i]:
                leaf[i] = True
                queue.append(i)
            toPrune[node] = 0

def bfs(root):
    queue = deque([root])
    visited = [False for i in range(n)]
    visited[root] = True
    diameter = 0
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            for next in graph[node]:
                if not visited[next] and toPrune[next] > 0:
                    queue.append(next)
                    visited[next] = True
        diameter += 1
    return [node, diameter-1]

root = -1
graphCount = -1
for i in range(n):
    if toPrune[i] > 0:
        if root < 0:
            root = i
        graphCount += 1
graphCount *= 2

print(graphCount - bfs(bfs(root)[0])[1])