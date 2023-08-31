n = int(input())
t = int(input())

trees = []
for i in range(t):
  trees.append([int(x) for x in input().split()])
trees.append([0, 0])
trees.append([n+1, n+1])

t += 2

maxSize = []
for x in range(t):
  x1, y1 = trees[x]
  
  for y in range(t):
    x2, y2 = trees[y]
    if x != y and x1 < x2 and y1 < y2:
      size = min(n-x1, y2-1)

      for z in range(t):
        x3, y3 = trees[z]
        if z != x and z != y and x3 > x1 and y3 < y2:
          size = min(size, max(x3-x1-1, y2-y3-1))
      maxSize.append(size)

print(max(maxSize))