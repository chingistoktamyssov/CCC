n = int(input())

a = []
b = []

for i in range(n):

  c = input()
  a.append(c)

for i in range(n):

  c = input()
  b.append(c)

common = sum(x == y for x,y in zip(a, b))

print(str(common))
