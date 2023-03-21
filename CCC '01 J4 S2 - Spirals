x = int(input())
y = int(input())

spiral = [[x]]
direction = 'D'
layer = 0
counter = 0
w = 0
z = 1
a = 0

for i in range(x + 1, y + 1):
  if direction == 'D':
    try:
      spiral[layer + 1].insert(0, i)
    except:
      spiral.append([i])
    finally:
      layer += 1
  elif direction == 'R':
    spiral[layer].insert(len(spiral[layer]), i)
  elif direction == 'U':
    if layer == 0:
      spiral.insert(0, [i])
    else:
      spiral[layer - 1].insert(len(spiral[layer - 1]), i)
      layer -= 1
  elif direction == 'L':
    spiral[layer].insert(0, i)

  counter += 1

  if counter == z:
    counter = 0
    w += 1
    if direction == 'D':
      direction = 'R'
    elif direction == 'R':
      direction = 'U'
    elif direction == 'U':
      direction = 'L'
    elif direction == 'L':
      direction = 'D'
    if w == 2:
      w = 0
      z += 1

for i in range(len(spiral)):
  for j in spiral[i]:
    l = len(str(j))
    if l >= a:
      a = l

for i in range(len(spiral)):
  for j in range(len(spiral[i])):
    if len(str(spiral[i][j])) < a:
      spiral[i][j] = ' ' * (a - len(str(spiral[i][j]))) + str(spiral[i][j])

for i in spiral:
  if len(i) < len(spiral[-1]):
    print(
      ' ' *
      (len(' '.join(str(x)
                    for x in spiral[-1])) - len(' '.join(str(x) for x in i))) +
      ' '.join(str(x) for x in i))
  else:
    print(' '.join(str(x) for x in i))
