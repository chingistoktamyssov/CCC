h = int(input())

column = list(range(1, h+1, 2))
column.extend(column[::-1][1:])

for x in column:
  print('*'*x + ' '*(2*h - 2*x) + '*'*x)