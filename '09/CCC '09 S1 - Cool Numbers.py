import math

count = 0

for i in range(math.floor(math.sqrt(int(input()))), math.floor(math.sqrt(int(input()))) + 1):
  x = str(round(math.pow(i ** 2, 1/3), 4))
  if x[-1] == '0':
    count += 1
    
print(count)