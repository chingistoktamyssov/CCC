c, r = [int(x) for x in input().split()]
current = [0, 0]

while 1:
  move = [int(x) for x in input().split()]
  if move == [0, 0]:
    break
    
  if current[0] + move[0] < 0:
    current[0] = 0
  elif current[0] + move[0] > c:
    current[0] = c
  else:
    current[0] += move[0]
    
  if current[1] + move[1] < 0:
    current[1] = 0
  elif current[1] + move[1] > r:
    current[1] = r
  else:
    current[1] += move[1]

  print(current[0], current[1])