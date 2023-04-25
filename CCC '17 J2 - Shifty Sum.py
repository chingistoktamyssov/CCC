n = int(input())
shift = int(input())
total = n

for i in range(shift):
  total = total + n * 10
  n = n * 10

print(total)