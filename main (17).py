bigwidth, bigheight, smallwidth, smallheight, steps = int(input()), int(input()), int(input()), int(input()), int(input())

stepped = []
position = [smallwidth+1, 1]
direction = ['right', 'down', 'Tright', 'down', 'left', 'Tdown', 'left', 'up', 'Tleft', 'up', 'right', 'Tup', 'DOG']
x = 0

for i in range(1, smallwidth+1):
  for j in range(1, smallheight+1):
    stepped.append([i, j])
for i in range(1, smallwidth+1):
  for j in range(bigheight-smallheight+1,bigheight+1):
    stepped.append([i, j])
for i in range(bigwidth-smallwidth+1, bigwidth+1):
  for j in range(1, smallheight+1):
    stepped.append([i, j])
for i in range(bigwidth-smallwidth+1, bigwidth+1):
  for j in range(bigheight-smallheight+1, bigheight+1):
    stepped.append([i, j])

def directioncycle(x):
  if x == 11:
    x = 0
  else:
    x += 1
  return x 

def move(direction, x, position):
  if direction[x] == 'right' or direction[x] == 'Tright':
    position[0] += 1
  elif direction[x] == 'down' or direction[x] == 'Tdown':
    position[1] += 1
  elif direction[x] == 'up' or direction[x] == 'Tup':
    position[1] -= 1
  elif direction[x] == 'left' or direction[x] == 'Tleft':
    position[0] -= 1
  return position
  
for i in range(steps):
  if direction[x] == 'right' or direction[x] == 'Tright':
    if direction[x+1] == 'Tup' and [position[0], position[1]-1] not in stepped and position[1]-1 != 0:
      x = directioncycle(x)
    elif [position[0]+1, position[1]] in stepped or position[0]+1 == bigwidth+1:
      x = directioncycle(x)
    
  elif direction[x] == 'down' or direction[x] == 'Tdown':
    if direction[x+1] == 'Tright' and [position[0]+1, position[1]] not in stepped and position[0]+1 != bigwidth+1:
      x = directioncycle(x)
    elif [position[0], position[1]+1] in stepped or position[1]+1 == bigheight+1:
      x = directioncycle(x)

  elif direction[x] == 'up' or direction[x] == 'Tup':
    if direction[x+1] == 'Tleft' and [position[0]-1, position[1]] not in stepped and position[0]-1 != 0:
      x = directioncycle(x)
    elif [position[0], position[1]-1] in stepped or position[1]-1 == 0:
      x = directioncycle(x)

  elif direction[x] == 'left' or direction[x] == 'Tleft':
    if direction[x+1] == 'Tdown' and [position[0], position[1]+1] not in stepped and position[1]+1 != bigheight+1:
      x = directioncycle(x)
    elif [position[0]-1, position[1]] in stepped or position[0]-1 == 0:
      x = directioncycle(x)

  if [position[0]+1,position[1]] in stepped and [position[0]-1,position[1]] in stepped and [position[0],position[1]+1] in stepped and [position[0],position[1]-1] in stepped:
    break

  stepped.append(position.copy())
  position = move(direction, x, position)

print(position[0])
print(position[1])