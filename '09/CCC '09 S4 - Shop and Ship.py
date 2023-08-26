import sys
input = sys.stdin.readline

n = int(input())
map = []
for i in range(n+1):
  map.append([0 for i in range(n+1)])

t = int(input())
for i in range(t):
  x, y, c = [int(x) for x in input().split()]
  map[x][y] = c
  map[y][x] = c

k = int(input())
pencils = {}
for i in range(k):
  z, p = [int(x) for x in input().split()]
  pencils[z] = p

d = int(input())

#DIJKSTRA
distance = [float('inf')] * (n+1)
distance[d] = 0
visited = [False] * (n+1)

for k in range(n):
  minval = float('inf')
  for i in range(1, n+1):
    if distance[i] < minval and visited[i] == False:
      minval = distance[i]
      u = i
  visited[u] = True
  for i in range(1, n+1):
    if map[u][i] != 0:
      distance[i] = min(distance[i], distance[u] + map[u][i])

paths = []
for i in pencils:
  if i == d:
    paths.append(pencils[i])
  else:
    paths.append(pencils[i] + distance[i])

print(min(paths))