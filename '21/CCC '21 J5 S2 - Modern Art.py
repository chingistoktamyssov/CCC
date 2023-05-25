x = int(input())
y = int(input())

row = [1] * x
column = [1] * y

count = 0

for i in range(int(input())):
  paint = input().split()
  
  if paint[0] == 'R':
    row[int(paint[1])-1] += 1
  else:
    column[int(paint[1])-1] += 1

for i in range(x):
  for j in range(y):
    if (row[i] + column[j]) % 2 != 0:
      count += 1

print(count)