a = 0
b = 0

p = input().split()

while p[0] != '7':
  
  if p[0] == '1':
    if p[1] == 'A':
      a = int(p[2])
    elif p[1] == 'B':
      b = int(p[2])
      
  elif p[0] == '2':
    if p[1] == 'A':
      print(a)
    elif p[1] == 'B':
      print(b)
      
  elif p[0] == '3':
    if p[1] == 'A' and p[2] == 'B':
      a = a + b
    elif p[1] == 'A' and p[2] == 'A':
      a = a + a
    elif p[1] == 'B' and p[2] == 'A':
      b = a + b
    elif p[1] == 'B' and p[2] == 'B':
      b = b + b
      
  elif p[0] == '4':
    if p[1] == 'A' and p[2] == 'B':
      a = a * b
    elif p[1] == 'A' and p[2] == 'A':
      a = a * a
    elif p[1] == 'B' and p[2] == 'A':
      b = b * a
    elif p[1] == 'B' and p[2] == 'B':
      b = b * b
      
  elif p[0] == '5':
    if p[1] == 'A' and p[2] == 'B':
      a = a - b
    elif p[1] == 'A' and p[2] == 'A':
      a = a - a
    elif p[1] == 'B' and p[2] == 'A':
      b = b - a
    elif p[1] == 'B' and p[2] == 'B':
      b = b - b
      
  elif p[0] == '6':
    if p[1] == 'A' and p[2] == 'B':
      a = a // b
    elif p[1] == 'A' and p[2] == 'A':
      a = a // a
    elif p[1] == 'B' and p[2] == 'A':
      b = b // a
    elif p[1] == 'B' and p[2] == 'B':
      b = b // b
      
  p = input().split()