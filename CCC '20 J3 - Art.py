x = []
y = []

for i in range(int(input())):
  coordinate = input().split(',')
  x.append(int(coordinate[0]))
  y.append(int(coordinate[1]))

minx, miny = min(x) - 1, min(y) - 1
maxx, maxy = max(x) + 1, max(y) + 1

print(str(minx) + ',' + str(miny))
print(str(maxx) + ',' + str(maxy))