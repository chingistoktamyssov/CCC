import math

while 1:
  n = int(input())
  if n == 0:
    break
    
  total = 0
  for i in range(1, n+1):
    total += int(math.sqrt(n**2 - i**2))
    total += 1
  total = total * 4 + 1

  print(total)