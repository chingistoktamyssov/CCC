time = int(input())

choret = []
a = 0

for i in range(int(input())):
  b = int(input())
  choret.append(b)
choret.sort()

for i in choret:
  time = time - i
  if time >= 0:
    a = a + 1
  else:
    break
    
print(a)