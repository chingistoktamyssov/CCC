r = 0
l = []
s = 0
t = 0

for i in range(4):
  m = input()
  n = m.split()
  n = [int(x) for x in n]
  l.append(n)

for i in range(4):
  for j in range(4):
    t = t + l[i][j]
  if i == 0:
    s = t
    t = 0
    r = r + 1
  elif t == s:
    t = 0
    r = r + 1
  else:
    t = 0

t = 0
    
for i in range(4):
  for j in range(4):
    t = t + l[j][i]
  if i == 0:
    t = 0
    r = r + 1
  elif t == s:
    t = 0
    r = r +1
  else:
    t = 0

if r == 8:
  print("magic")
else:
  print("not magic")
