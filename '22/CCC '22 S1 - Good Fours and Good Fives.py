n = int(input())
ways = 0

for i in range(n//5 + 1):
  if (n - i * 5) % 4 == 0:
    ways += 1

print(ways)