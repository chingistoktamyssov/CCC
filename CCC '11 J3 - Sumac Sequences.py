a = int(input())
b = int(input())

d = 2

while True:
  d += 1
  c = a - b
  
  if c <= b:
    pass
  else:
    break
    
  a = b
  b = c
  
print(d)