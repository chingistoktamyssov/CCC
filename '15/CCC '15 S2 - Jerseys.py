sizes = {'S': 1, 'M': 2, 'L': 3}

j = int(input())
a = int(input())

jerseys = {}
for i in range(j):
  jerseys[str(i+1)] = sizes[input()]

n = 0

for i in range(a):
  player = input().split()
  if jerseys[player[1]] >= sizes[player[0]]:
    n += 1
    jerseys[player[1]] = 0

print(n)