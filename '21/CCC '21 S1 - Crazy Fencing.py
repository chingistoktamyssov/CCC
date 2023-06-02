n = int(input())
side = [int(x) for x in input().split()]
base = [int(x) for x in input().split()]

area = 0
for i in range(n):
  area += (side[i] + side[i+1])/2 * base[i]

print(area)