a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

x = s

nikky = 0
front = True

while s > 0:
  if front == True:
    if s - a < 0:
      nikky += s
      s = 0
    else:
      nikky += a
      s = s - a
      front = False
  elif front == False:
    if s - b < 0:
      nikky -= s
      s = 0
    else:
      nikky -= b
      s = s - b
      front = True

byron = 0
front = True

while x > 0:
  if front == True:
    if x - c < 0:
      byron += x
      x = 0
    else:
      byron += c
      x = x - c
      front = False
  elif front == False:
    if x - d < 0:
      byron -= x
      x = 0
    else:
      byron -= d
      x = x -d
      front = True
      
if nikky > byron:
  print('Nikky')
elif byron > nikky:
  print('Byron')
else:
  print('Tied')