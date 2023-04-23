position = 1

def snakes(position):
  if position == 54:
    return 19
  elif position == 90:
    return 48
  elif position == 99:
    return 77
  else:
    return position

def ladders(position):
  if position == 9:
    return 34
  elif position == 40:
    return 64
  elif position == 67:
    return 86
  else:
    return position

while True:
  roll = int(input())
  
  if roll == 0:
    print('You Quit!')
    break
    
  else:
    if position + roll > 100:
      print('You are now on square', position)
      
    else:
      position += roll
      
      position = ladders(position)
      position = snakes(position)
      
      print('You are now on square', position)
      if position == 100:
        print('You Win!')
        break
