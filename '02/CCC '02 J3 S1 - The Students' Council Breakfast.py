pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())

combo = []

for a in range(0, total//pink+1):
  for b in range(0, total//green+1):
    for c in range(0, total//red+1):
      for d in range(0, total//orange+1):
        if a * pink + b * green + c * red + d * orange == total:
          combo.append([a, b, c, d])

for i in range(len(combo)):
  print('# of PINK is', combo[i][0], '# of GREEN is', combo[i][1], '# of RED is', combo[i][2], '# of ORANGE is', combo[i][3])

print('Total combinations is ' + str(len(combo)) + '.')

for i in range(len(combo)):
  if i == 0:
    minimum = combo[i][0] + combo[i][1] + combo[i][2] + combo[i][3]
  else:
    if combo[i][0] + combo[i][1] + combo[i][2] + combo[i][3] < minimum:
      minimum = combo[i][0] + combo[i][1] + combo[i][2] + combo[i][3]

print('Minimum number of tickets to print is ' + str(minimum) + '.')  
