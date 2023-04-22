a, b = 100, 100

for i in range(int(input())):
  c = [int(x) for x in input().split()]
  
  if c[0] > c[1]:
    b = b - c[0]
  elif c[0] < c[1]:
    a = a - c[1]
    
print(a)
print(b)