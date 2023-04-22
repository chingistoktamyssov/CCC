drilled = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4],
           [3, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3],
           [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7],
           [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6], [-1, -5]]
position = [-1, -5]

move = input().split()

x = True
y = True

while move[0] != 'q' and y == True:
  
  if move[0] == 'l':
    for i in range(int(move[1])):
      position[0] -= 1
      if position in drilled:
        x = False
      else:
        a = position.copy()
        drilled.append(a)
    if x == True:
      print(position[0], position[1], 'safe')
    else:
      print(position[0], position[1], 'DANGER')
      y = False
      
  elif move[0] == 'r':
    for i in range(int(move[1])):
      position[0] += 1
      if position in drilled:
        x = False
      else:
        a = position.copy()
        drilled.append(a)
    if x == True:
      print(position[0], position[1], 'safe')
    else:
      print(position[0], position[1], 'DANGER')
      y = False
      
  elif move[0] == 'u':
    for i in range(int(move[1])):
      position[1] += 1
      if position in drilled:
        x = False
      else:
        a = position.copy()
        drilled.append(a)
    if x == True:
      print(position[0], position[1], 'safe')
    else:
      print(position[0], position[1], 'DANGER')
      y = False
      
  elif move[0] == 'd':
    for i in range(int(move[1])):
      position[1] -= 1
      if position in drilled:
        x = False
      else:
        a = position.copy()
        drilled.append(a)
    if x == True:
      print(position[0], position[1], 'safe')
    else:
      print(position[0], position[1], 'DANGER')
      y = False
      
  if y == True:
    move = input().split()