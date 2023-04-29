a = str(int(input()) + 1)

while True:
  
  d = ''
  c = 0
  b = []
  a = list(a)
  
  for x in range(len(a)):
    if x == 0:
      b.append(a[x])
    else:
      if a[x] in b:
        c = 1
      else:
        b.append(a[x])
        
  for x in a:
    d += x
  d = int(d)
  
  if c == 1:
    d += 1
    a = d
    a = str(a)
    
  else:
    print(d)
    break