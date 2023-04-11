directions = []
locations = []

while True:
  x = input()
  if x == 'SCHOOL':
    break
  if x == 'L' or x == 'R':
    directions.append(x)
  else:
    locations.append(x)

directions.reverse()
locations.reverse()
locations.append('HOME')

for i in range(len(directions)):
  if directions[i] == 'L':
    directions[i] = 'RIGHT'
  elif directions[i] == 'R':
    directions[i] = 'LEFT'

for i in range(len(locations)):
  if i == len(locations) - 1:
    print('Turn ' + str(directions[i]) + ' into your ' + str(locations[i]) +
          '.')
  else:
    print('Turn ' + str(directions[i]) + ' onto ' + str(locations[i]) +
          ' street.')