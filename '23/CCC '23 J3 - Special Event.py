days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for i in range(int(input())):
  person = list(input())
  for j in range(len(person)):
    if person[j] == 'Y':
      days[j + 1] = days[j + 1] + 1
    
good = []

for i in range(len(days)):
  if i == 0:
    a = days[i + 1]
    good.append(i + 1)
  elif days[i + 1] > a:
    good = []
    good.append(i + 1)
    a = days[i + 1]
  elif days[i + 1] == a:
    good.append(i + 1)
    
b = ''

if len(good) == 1:
  print(good[0])
else:
  for i in range(len(good)):
    if i + 1 == len(good):
      b = b + str(good[i])
    else:
      b = b + str(good[i]) + ","
      
  print(b)