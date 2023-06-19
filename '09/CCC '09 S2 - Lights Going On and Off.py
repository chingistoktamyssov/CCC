row, column = int(input()), int(input())

lights = []
for i in range(row):
  lights.append(input().split())

original = []

for x in lights:
  original.append(x.copy())
  
pattern = [lights[-1].copy()]

for i in range(1, row+1):
  for j in range(i, row):
    for i in range(column):
      if lights[j-1][i] == lights[j][i]:
        lights[j][i] = '0'
      else:
        lights[j][i] = '1'
        
    if lights[-1].copy() not in pattern:
      pattern.append(lights[-1].copy())

  lights = []
  for x in original:
    lights.append(x.copy())

print(len(pattern))