violations = 0

same = {}
notsame = {}

for i in range(int(input())):
  x = input().split()
  if x[0] in same.keys():
    same[x[0]].append(x[1])
  else:
    same[x[0]] = [x[1]] 

for i in range(int(input())):
  x = input().split()
  if x[0] in notsame.keys():
    notsame[x[0]].append(x[1])
  else:
    notsame[x[0]] = [x[1]] 

for i in range(int(input())):
  group = input().split()
  for j in group:
    if j in same.keys():
      for k in same[j]:
        if k not in group:
          violations += 1

    if j in notsame.keys():
      for k in notsame[j]:
        if k in group:
          violations += 1
      
print(violations)