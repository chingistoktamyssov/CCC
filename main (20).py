n, m = int(input()), int(input())

ways = 0

for i in range(1, n+1):
  for j in range(1, m+1):
    if i + j == 10:
      ways += 1

if ways == 1:
  print('There is 1 way to get the sum 10.')
else:
  print('There are ' + str(ways) + ' ways to get the sum 10.')