x = int(input())
m = int(input())

for i in range(m+1):
  if (x * i) % m == 1:
    print(i)
    break
  elif i == m:
    print('No such integer exists.')
